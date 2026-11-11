import sys
from pathlib import Path
from typing import TypedDict

from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langgraph.graph import END, START, StateGraph

from job_fit_agent.compare import compare
from job_fit_agent.extract import extract
from job_fit_agent.models import (
    CandidateProfile,
    JobPosting,
    SkillComparison,
    StudyPlan,
)
from job_fit_agent.plan import make_plan
from job_fit_agent.profile import my_profile
from job_fit_agent.report import to_markdown


class State(TypedDict):
    job_text: str
    job: JobPosting | None
    profile: CandidateProfile
    comparison: SkillComparison | None
    plan: StudyPlan | None


def extract_job(state: State) -> dict:
    # Node, state'in tamamını değil sadece değiştirdiği kısmı döndürür
    return {"job": extract(state["job_text"])}


def compare_profile(state: State) -> dict:
    # extract_job'un doldurduğu state["job"]'u kullanır
    return {"comparison": compare(state["job"].required_skills, state["profile"])}


def plan_study(state: State) -> dict:
    return {"plan": make_plan(state["comparison"])}


def has_gaps(state: State) -> str:
    # "yok" veya "kısmen" varsa "make_plan", yoksa END döndür
    if any(m.status in ("yok", "kısmen") for m in state["comparison"].matches):
        return "make_plan"
    return END


builder = StateGraph(State)
builder.add_node("extract_job", extract_job)
builder.add_node("compare_profile", compare_profile)
builder.add_node("make_plan", plan_study)
builder.add_edge(START, "extract_job")
builder.add_edge("extract_job", "compare_profile")
builder.add_conditional_edges("compare_profile", has_gaps)
builder.add_edge("make_plan", END)
graph = builder.compile()


def analyze(job_text: str, profile: CandidateProfile) -> str:
    """Grafı çalıştırır ve sonucu Markdown rapor olarak döndürür."""
    final_state = graph.invoke(
        {
            "job_text": job_text,
            "job": None,
            "profile": profile,
            "comparison": None,
            "plan": None,
        },
        # Her node ve model çağrısı Langfuse'a kaydedilir
        config={"callbacks": [CallbackHandler()]},
    )
    # Uzun süre açık kalan sunucuda kayıtlar beklemeden gönderilsin
    get_client().flush()
    return to_markdown(final_state["job"], final_state["comparison"], final_state["plan"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Kullanım: python src/job_fit_agent/graph.py jobs/<ilan>.txt")

    job_path = Path(sys.argv[1])
    report = analyze(job_path.read_text(encoding="utf-8"), my_profile)

    report_path = Path("reports") / f"{job_path.stem}.md"  # jobs/qnb.txt → reports/qnb.md
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"Rapor kaydedildi: {report_path}")

    # Arka planda bekleyen kayıtları göndermeden script'i kapatma
    get_client().shutdown()
