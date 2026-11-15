"""Uyum skoru: modele sorulmaz, sabit bir formülle kodda hesaplanır.

skor = (var × 1 + kısmen × 0.5) / zorunlu beceri sayısı × 100
Artı beceriler skoru etkilemez; tüm zorunlular varsa artılar yüzünden skor düşmez.
"""

from pydantic import BaseModel

from job_fit_agent.models import CandidateProfile, JobPosting, SkillComparison, split_matches

# Bundan az zorunlu beceri varsa skor büyük ihtimalle extract'ın beceri kaçırmasından
# etkileniyor: skor, altındaki veri kadar güvenilir.
MIN_REQUIRED = 5
WEIGHTS = {"var": 1.0, "kısmen": 0.5, "yok": 0.0}


class FitScore(BaseModel):
    score: int  # 0-100
    required_total: int
    low_confidence: bool  # zorunlu beceri < MIN_REQUIRED
    experience_ok: bool | None  # ilan min. yıl istiyorsa profil karşılıyor mu; skoru etkilemez


def fit_score(
    job: JobPosting, comparison: SkillComparison, profile: CandidateProfile
) -> FitScore:
    required, _ = split_matches(job, comparison)
    total = len(required)
    points = sum(WEIGHTS[m.status] for m in required)
    score = round(points / total * 100) if total else 0

    experience_ok = (
        None
        if job.min_years_experience is None
        else profile.years_experience >= job.min_years_experience
    )
    return FitScore(
        score=score,
        required_total=total,
        low_confidence=total < MIN_REQUIRED,
        experience_ok=experience_ok,
    )
