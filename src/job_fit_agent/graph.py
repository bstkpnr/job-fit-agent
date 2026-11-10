from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from job_fit_agent.extract import QNB_JOB_POSTING, extract
from job_fit_agent.models import JobPosting


class State(TypedDict):
    job_text: str
    job: JobPosting | None


def extract_job(state: State) -> dict:
    # Node, state'in tamamını değil sadece değiştirdiği kısmı döndürür
    return {"job": extract(state["job_text"])}


builder = StateGraph(State)
builder.add_node("extract_job", extract_job)
builder.add_edge(START, "extract_job")
builder.add_edge("extract_job", END)
graph = builder.compile()


if __name__ == "__main__":
    final_state = graph.invoke({"job_text": QNB_JOB_POSTING, "job": None})
    print(final_state["job"].required_skills)
