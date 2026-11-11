import numpy as np
from langchain_anthropic import ChatAnthropic

from job_fit_agent.extract import QNB_JOB_POSTING, extract
from job_fit_agent.match import cosine, model
from job_fit_agent.models import CandidateProfile, SkillComparison
from job_fit_agent.profile import my_profile

INSTRUCTION = """\
Aşağıda bir iş ilanındaki beceriler var. Her birinin yanında, adayın profilinden
anlamca en yakın görünen 3 beceri aday olarak verilmiş.

Her ilan becerisi için adayın durumunu belirle:
- "var": Aynı beceri ya da onu açıkça kapsayan bir beceri.
- "kısmen": İlgili ama aynı değil.
- "yok": Adaylardan hiçbiri gerçekten ilgili değil.

Kurallar:
- Adaylar sadece öneri; benzer görünüyor diye eşleştirme.
- İyimser olma: Emin değilsen "kısmen" ya da "yok" de.
- matched_with alanına sadece adaylardan birini yaz; "yok" ise boş bırak.
- reason alanı kısa olsun (en fazla bir cümle).
- Her ilan becerisi için tam olarak bir sonuç döndür.
"""


def top_candidates(
    job_skills: list[str], my_skills: list[str], k: int = 3
) -> list[tuple[str, list[str]]]:
    # Her listeyi tek seferde embed ediyoruz
    job_vectors = list(model.embed(job_skills))
    my_vectors = list(model.embed(my_skills))

    result = []
    for job_skill, job_vec in zip(job_skills, job_vectors):
        scores = [cosine(job_vec, my_vec) for my_vec in my_vectors]
        top = np.argsort(scores)[-k:][::-1]  # en yüksek k skorun sırası, büyükten küçüğe
        result.append((job_skill, [my_skills[i] for i in top]))
    return result


def compare(job_skills: list[str], profile: CandidateProfile) -> SkillComparison:
    candidates = top_candidates(job_skills, profile.skills)
    lines = "\n".join(
        f"- {job_skill} (adaylar: {', '.join(cands)})" for job_skill, cands in candidates
    )

    llm = ChatAnthropic(model="claude-sonnet-5-5")
    structured_llm = llm.with_structured_output(SkillComparison, method="json_schema")
    return structured_llm.invoke(f"{INSTRUCTION}\n{lines}")


if __name__ == "__main__":
    job_skills = extract(QNB_JOB_POSTING).required_skills

    comparison = compare(job_skills, my_profile)
    for m in comparison.matches:
        matched = f"({m.matched_with})" if m.matched_with else ""
        print(f"{m.job_skill:<26} → {m.status:<7} {matched:<22} {m.reason}")
