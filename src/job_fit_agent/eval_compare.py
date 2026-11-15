import json
import sys
from pathlib import Path

from job_fit_agent.compare import compare
from job_fit_agent.profile import my_profile

# Doğru cevaplar (golden set): kendi deneyimime göre, evals/golden.json'da
GOLDEN_PATH = Path(__file__).resolve().parents[2] / "evals" / "golden.json"
GOLDEN: dict[str, str] = json.loads(GOLDEN_PATH.read_text(encoding="utf-8"))

RUNS = 3


if __name__ == "__main__":
    missing = [s for s, label in GOLDEN.items() if label not in ("var", "kısmen", "yok")]
    if missing:
        sys.exit(f"Etiketlenmemiş maddeler var: {', '.join(missing)}")

    # Her beceri için her çalıştırmanın sonucunu topla
    results: dict[str, list[str | None]] = {skill: [] for skill in GOLDEN}
    for _ in range(RUNS):
        result = compare(list(GOLDEN), my_profile)
        # Golden anahtarları küçük harf; model "Python" yazarsa da eşleşsin
        statuses = {m.job_skill.lower(): m.status for m in result.matches}
        for skill in GOLDEN:
            # Model beceri adını değiştirirse None döner ve yanlış sayılır
            results[skill].append(statuses.get(skill.lower()))

    correct_total = 0
    consistent = 0
    for skill, expected in GOLDEN.items():
        got = results[skill]
        correct = sum(1 for s in got if s == expected)
        correct_total += correct
        if len(set(got)) == 1:
            consistent += 1
        shown = ", ".join(s or "-" for s in got)
        print(
            f"{skill:<22} beklenen: {expected:<7} sonuçlar: {shown:<24} {correct}/{RUNS}"
        )

    total = len(GOLDEN) * RUNS
    print()
    print(f"Doğruluk:   {correct_total}/{total} ({correct_total / total:.0%})")
    print(
        f"Tutarlılık: {consistent}/{len(GOLDEN)} ({consistent / len(GOLDEN):.0%})"
    )
