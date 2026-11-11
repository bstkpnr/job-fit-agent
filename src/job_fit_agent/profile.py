from job_fit_agent.extract import QNB_JOB_POSTING, extract
from job_fit_agent.models import CandidateProfile

my_profile = CandidateProfile(
    name="Beste Tokpınar Boğa",
    skills=[
        # Mobil ve web
        "React Native",
        "ReactJS",
        "TypeScript",
        "JavaScript",
        "Redux",
        "Context API",
        "HTML",
        "CSS",
        "SASS",
        "Tailwind",
        "Bootstrap",
        "jQuery",
        # Backend
        "C#",
        ".NET",
        "SQL",
        "Firebase",
        "Node.js",
        "Express",
        "REST APIs",
        "FastAPI",
        "Microservices",
        # Yapay zekâ (CV + Harcama Koçu ve RAG servisi)
        "Python",
        "RAG",
        "Tool Calling",
        "Prompt Engineering",
        "Context Engineering",
        "Embedding Models",
        "Azure OpenAI",
        "LLMs",
        "AI Agents",
        "Machine Learning",
        "Predictive Modeling",
        "LangGraph",
        "LangChain",
        "Structured Output", "Pydantic", "Vector Databases", "Qdrant", "Hybrid Search", "Streaming", "Prompt Caching",

        # Entegrasyon ve alan bilgisi
        "Bluetooth Low Energy",
        "SDK Integration",
        "KYC",
        "Payment Systems",
        # Araçlar
        "Git",
        "CI/CD",
        "Azure DevOps",
        "GitHub Actions",
    ],
    years_experience=4,  # Ocak 2022 - bugün (staj hariç)
)


if __name__ == "__main__":
    job_skills = extract(QNB_JOB_POSTING).required_skills

    # Büyük/küçük harf farkı eşleşmeyi bozmasın diye hepsini küçük harfe çeviriyoruz
    ilan = {s.lower() for s in job_skills}
    ben = {s.lower() for s in my_profile.skills}

    ortak = ilan & ben  # iki listede de olanlar
    eksik = ilan - ben  # ilanda olup bende olmayanlar

    print("İlan becerileri:", sorted(ilan))
    print()
    print(f"Ortak ({len(ortak)}):", sorted(ortak))
    print()
    print(f"Eksik ({len(eksik)}):", sorted(eksik))
