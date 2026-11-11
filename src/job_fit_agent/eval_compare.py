from job_fit_agent.compare import compare
from job_fit_agent.profile import my_profile

# Doğru cevaplar (golden set): kendi deneyimime göre
GOLDEN = {
    "Function Calling": "var",
    "MCP": "yok",
    "LoRA": "yok",
    "Fine-tuning": "kısmen",
    "Software Engineering": "var",
    "Context Engineering": "var",
    "LangChain": "var",
    "Output Validation": "var",
    "Multi-agent Workflows": "kısmen",
    "Guardrails": "kısmen",
    "Microservices": "var",
    "LLM APIs": "var",
}

RUNS = 3


if __name__ == "__main__":
    # Her beceri için her çalıştırmanın sonucunu topla
    results: dict[str, list[str | None]] = {skill: [] for skill in GOLDEN}
    for _ in range(RUNS):
        result = compare(list(GOLDEN), my_profile)
        statuses = {m.job_skill: m.status for m in result.matches}
        for skill in GOLDEN:
            # Model beceri adını değiştirirse None döner ve yanlış sayılır
            results[skill].append(statuses.get(skill))

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
