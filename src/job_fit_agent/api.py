"""İş ilanı analizini HTTP üzerinden sunan FastAPI uygulaması.

Akış: Gmail → n8n → POST /analyze → n8n → cevap e-postası
Çalıştırma: uv run --env-file .env uvicorn job_fit_agent.api:app --reload
"""

import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from job_fit_agent.graph import run
from job_fit_agent.models import JobPosting, SkillComparison, StudyPlan
from job_fit_agent.profile import my_profile
from job_fit_agent.report import to_markdown
from job_fit_agent.score import FitScore, fit_score

app = FastAPI(title="job-fit-agent")


class AnalyzeRequest(BaseModel):
    # Kısa/boş metin model çağrısına ulaşmasın, çok uzun metin maliyeti şişirmesin.
    # Kurala uymayan isteği FastAPI kendisi 422 ile reddeder.
    job_text: str = Field(min_length=200, max_length=20000)


class AnalyzeResponse(BaseModel):
    job: JobPosting
    comparison: SkillComparison
    plan: StudyPlan | None
    score: FitScore
    markdown: str  # n8n bunu doğrudan e-posta gövdesine koyacak


def check_api_key(x_api_key: str | None = Header(default=None)) -> None:
    expected = os.environ.get("API_KEY")
    # Anahtar tanımlı değilse kapıyı açık bırakma: her çağrı para harcıyor
    if not expected:
        raise HTTPException(status_code=500, detail="Sunucuda API_KEY tanımlı değil")
    # compare_digest: karşılaştırma süresinden anahtar tahmin edilemesin
    if x_api_key is None or not secrets.compare_digest(x_api_key, expected):
        raise HTTPException(status_code=401, detail="Geçersiz API anahtarı")


# DİKKAT: async def değil. graph.invoke ~25 sn bloklar; async def içinde olsaydı
# bu sürede sunucu başka isteğe cevap veremezdi. Düz def'i FastAPI ayrı bir
# thread'de çalıştırır, sunucu donmaz.
# dependencies: anahtar, gövde doğrulamasından önce kontrol edilir (yanlış anahtar → 401)
@app.post("/analyze", dependencies=[Depends(check_api_key)])
def analyze_job(req: AnalyzeRequest) -> AnalyzeResponse:
    state = run(req.job_text, my_profile)
    job, comparison, plan = state["job"], state["comparison"], state["plan"]
    return AnalyzeResponse(
        job=job,
        comparison=comparison,
        plan=plan,
        score=fit_score(job, comparison, my_profile),
        markdown=to_markdown(job, comparison, plan),
    )
