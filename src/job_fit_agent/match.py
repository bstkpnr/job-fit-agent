import numpy as np
from fastembed import TextEmbedding

from job_fit_agent.extract import QNB_JOB_POSTING
from job_fit_agent.graph import graph
from job_fit_agent.profile import my_profile

model = TextEmbedding("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def match_skills(
    job_skills: list[str], my_skills: list[str]
) -> list[tuple[str, str, float]]:
    # Her listeyi tek seferde embed ediyoruz, tek tek göndermekten çok daha hızlı
    job_vectors = list(model.embed(job_skills))
    my_vectors = list(model.embed(my_skills))

    matches = []
    for job_skill, job_vec in zip(job_skills, job_vectors):
        scores = [cosine(job_vec, my_vec) for my_vec in my_vectors]
        best = int(np.argmax(scores))  # en yüksek skorun sırası
        matches.append((job_skill, my_skills[best], scores[best]))

    return sorted(matches, key=lambda m: m[2], reverse=True)


if __name__ == "__main__":
    # Görev 1: küçük deneme
    tool, function, css = list(model.embed(["Tool Calling", "Function Calling", "CSS"]))
    print(f"Tool Calling ~ Function Calling: {cosine(tool, function):.3f}")
    print(f"Tool Calling ~ CSS:              {cosine(tool, css):.3f}")
    print()

    # Görev 2: asıl eşleştirme
    final_state = graph.invoke({"job_text": QNB_JOB_POSTING, "job": None})
    job_skills = final_state["job"].required_skills

    for job_skill, my_skill, score in match_skills(job_skills, my_profile.skills):
        print(f"{score:.3f}  {job_skill:<35} → {my_skill}")
