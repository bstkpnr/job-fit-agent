from pathlib import Path

from langchain_anthropic import ChatAnthropic

from job_fit_agent.models import JobPosting

INSTRUCTION = (
    "Bu iş ilanından bilgileri çıkar. "
    "Sadece ilanda yazanı kullan, ilanda olmayan bir bilgiyi uydurma."
)

# Test bloklarında kullanılan kurgusal örnek ilan (repoda tek ilan bu)
EXAMPLE_JOB_POSTING = (
    Path(__file__).resolve().parents[2] / "jobs" / "example.txt"
).read_text(encoding="utf-8")


def extract(text: str) -> JobPosting:
    llm = ChatAnthropic(model="claude-sonnet-5-5")
    # cevabı bu şekle zorla
    structured_llm = llm.with_structured_output(JobPosting, method="json_schema")

    return structured_llm.invoke(f"{INSTRUCTION}\n\n{text}")


if __name__ == "__main__":
    print(extract(EXAMPLE_JOB_POSTING))
