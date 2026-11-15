"""reports/*.json → ilanları uyum skoruna göre sıralar.

Çalıştırma: uv run python src/job_fit_agent/rank.py
"""

import json
from pathlib import Path

from job_fit_agent.export_demo import EXCLUDE, LABELS
from job_fit_agent.models import JobPosting, SkillComparison
from job_fit_agent.profile import my_profile
from job_fit_agent.score import fit_score

REPORTS = Path(__file__).resolve().parents[2] / "reports"

rows = []
for path in sorted(REPORTS.glob("*.json")):
    if path.stem in EXCLUDE:
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    job = JobPosting.model_validate(data["job"])
    comparison = SkillComparison.model_validate(data["comparison"])
    fit = fit_score(job, comparison, my_profile)
    # Demodaki anonim etiketi kullan; etiketi yoksa dosya adını göster
    label = LABELS.get(path.stem, path.stem)
    rows.append((fit, f"{label} — {job.title}"))

# Düşük güvenliler en altta, kendi içlerinde de skora göre.
# Eşit skorda ada göre: dosya okuma sırası sistemden sisteme değişebilir.
rows.sort(key=lambda r: (r[0].low_confidence, -r[0].score, r[1]))

for fit, name in rows:
    flags = []
    if fit.low_confidence:
        flags.append("⚠ düşük güven")
    if fit.experience_ok is False:
        flags.append("⚠ deneyim")
    flag_text = "  ".join(flags)
    print(f"{fit.score:>3}  {name:<62} ({fit.required_total} zorunlu)  {flag_text}".rstrip())
