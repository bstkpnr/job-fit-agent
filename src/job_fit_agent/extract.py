from langchain_anthropic import ChatAnthropic

from job_fit_agent.models import JobPosting

INSTRUCTION = (
    "Bu iş ilanından bilgileri çıkar. "
    "Sadece ilanda yazanı kullan, ilanda olmayan bir bilgiyi uydurma."
)

QNB_JOB_POSTING = """\
AI ENGINEER / AI AGENT DEVELOPER

QNB is always supporting employees who are eager to create a development at their career and
the future of the sector. Our human resources policies are aiming to create an equal, fulfilled and
empowering working atmosphere for individuals willing to have a satisfying career journey.

We're growing our AI team and looking for an engineer with hands-on experience building AI
agents. You'll work on agentic systems from design to production, together with a team that
builds everything in-house.

In this role, you will:
- Design, develop, and maintain LLM-based AI agents and multi-agent workflows that automate
  and enhance internal and customer-facing banking processes
- Architect end-to-end agentic systems, including orchestration, tool and function calling,
  memory, retrieval (RAG), and skill/connector integrations
- Hands-on experience with tool-use design, multi-agent architectures, and Model Context
  Protocol (MCP)
- Integrate AI agents with internal banking systems, APIs, databases, and enterprise data
  sources in a secure and scalable way
- Build and maintain guardrails, output validation, and safety layers so agent behavior stays
  accurate, compliant, and aligned with regulatory and data privacy requirements
- Apply prompt engineering, context engineering, and fine-tuning techniques (e.g. LoRA)
  to optimize model performance for banking-domain use cases
- Collaborate closely with cross-functional teams, particularly IT, security, and business
  units, to define, prioritize, and deliver AI projects
- Keep up with the latest developments in LLMs, agent frameworks, and AI tooling, and
  evaluate new technologies for adoption

We are waiting for your application if you have:
- A bachelor's degree from a reputable university, preferably in Computer Engineering,
  Software Engineering, Mathematics, or a related field
- Minimum 3-4 years of experience in AI engineering or related roles, including hands-on
  experience building LLM-based applications
- Strong proficiency in Python and solid software engineering practices
- Hands-on experience with LLM APIs and agent frameworks or orchestration tools (e.g.
  LangChain, LangGraph, LlamaIndex, Langflow, or similar)
- Experience with RAG architectures, vector databases, and embedding models
- Familiarity with REST APIs and microservices
"""


def extract(text: str) -> JobPosting:
    llm = ChatAnthropic(model="claude-sonnet-5-5")
    # cevabı bu şekle zorla
    structured_llm = llm.with_structured_output(JobPosting, method="json_schema")

    return structured_llm.invoke(f"{INSTRUCTION}\n\n{text}")


if __name__ == "__main__":
    print(extract(QNB_JOB_POSTING))
