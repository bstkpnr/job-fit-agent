import json
from collections import Counter
from pathlib import Path

# İlanlar arası aynı kavramın farklı adları → tek ad.
# Sadece sayımda kullanılır; raporlar ve compare kararı beceri adından etkilenmiyor.
# "kyc automation" bilerek yok: KYC bilmek ile KYC süreçlerini otomatikleştirmek farklı.
ALIASES = {
    "llm": "llms",
    "model context protocol": "mcp",
    "embedding models": "embeddings",
    "async programming": "asyncio",
    "agentic ai": "ai agents",
}

# reports/*.json dosyalarındaki ilan becerilerini toplayıp sayar
counts: Counter[str] = Counter()
files = sorted(Path("reports").glob("*.json"))
for path in files:
    job = json.loads(path.read_text(encoding="utf-8"))["job"]
    skills = job["required_skills"] + job["nice_to_have"]
    names = (s.lower() for s in skills)
    # Aynı ilanda iki kez geçen beceri bir kez sayılsın
    counts.update({ALIASES.get(n, n) for n in names})

print(f"{len(files)} ilan, {len(counts)} farklı beceri\n")
# Eşit sayıdakiler alfabetik: çıktı her çalıştırmada aynı olsun
for skill, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"{n:<3}{skill}")
