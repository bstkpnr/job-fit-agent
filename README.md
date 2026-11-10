# job-fit-agent

Bir iş ilanını okuyup adayın profiliyle karşılaştıran bir yapay zekâ agent'ı. İlandaki her beceri için adayda **var**, **kısmen** ya da **yok** kararı verir ve kısa bir gerekçe yazar.

LangGraph, Claude (Anthropic) ve Pydantic ile geliştiriliyor. Proje adım adım büyüyor; şu an ilanı çözümleme ve beceri karşılaştırma kısmı hazır.

## Nasıl çalışır?

```
İlan metni
   │
   ▼
1. Çıkarma (extract.py)       Claude ilanı okur → JobPosting
   │                           (başlık, şirket, beceriler, deneyim yılı)
   ▼
2. Aday bulma (match.py)      Embedding ile her ilan becerisi için
   │                           profildeki en yakın 3 beceri
   ▼
3. Karar (compare.py)         Claude adayları değerlendirir →
                               var / kısmen / yok + gerekçe
```

**Neden iki aşamalı eşleştirme?** Sadece embedding kullanınca kelimesi benzeyen ama anlamı farklı beceriler yüksek skor alıyor: örneğin `LoRA → RAG` (0.71) ya da `Context Engineering → Context API` (0.86). Embedding hızlı bir ön eleme yapıyor, son kararı LLM veriyor. LLM'e "benzer görünüyor diye eşleştirme, emin değilsen iyimser olma" kuralı veriliyor.

Örnek çıktı:

```
Function calling     → var     (Tool Calling)   Function calling, tool calling ile aynı mekanizmadır.
LangChain            → kısmen  (LangGraph)      LangGraph bilgisi LangChain öğrenmeyi kolaylaştırır.
LoRA                 → yok                      Adaylar LoRA ile ilgili değil.
```

## Dosyalar

| Dosya | Ne yapar |
|---|---|
| `models.py` | Pydantic modelleri: `JobPosting`, `CandidateProfile`, `SkillMatch`, `SkillComparison` |
| `extract.py` | İlan metninden yapılandırılmış bilgi çıkarır (`with_structured_output`) |
| `graph.py` | LangGraph akışı (şimdilik tek node: `extract_job`) |
| `profile.py` | Aday profili |
| `match.py` | `fastembed` ile becerileri anlamsal olarak eşleştirir |
| `compare.py` | Embedding adaylarını LLM ile değerlendirir |

## Kurulum

[uv](https://docs.astral.sh/uv/) gerekli.

```bash
git clone https://github.com/bstkpnr/job-fit-agent.git
cd job-fit-agent
uv sync
```

Proje kök klasöründe bir `.env` dosyası oluşturup Anthropic API anahtarını ekle:

```
ANTHROPIC_API_KEY=...
```

## Çalıştırma

Komutları proje kök klasöründen çalıştır:

```bash
# İlandan bilgi çıkar
uv run --env-file .env python src/job_fit_agent/extract.py

# Beceri karşılaştırması
uv run --env-file .env python src/job_fit_agent/compare.py
```

İlk çalıştırmada embedding modeli (`paraphrase-multilingual-MiniLM-L12-v2`) indirilir.

Kendi profilinle denemek için `profile.py` içindeki beceri listesini ve deneyim yılını değiştir.

## Yol haritası

- [x] İlandan yapılandırılmış bilgi çıkarma
- [x] İlk LangGraph akışı
- [x] Embedding + LLM ile beceri karşılaştırma
- [ ] Karşılaştırmayı LangGraph'a node olarak eklemek
- [ ] Eksik becerilere göre bir öğrenme planı çıkaran node
