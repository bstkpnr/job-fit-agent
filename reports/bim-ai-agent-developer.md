# Yapay Zeka / AI Agent Geliştirici — BİM Birleşik Mağazalar A.Ş.

**var: 15 · kısmen: 12 · yok: 3**

## Var

- **Machine Learning** (Machine Learning) — Profilde Machine Learning doğrudan listelenmiş.
- **Artificial Intelligence** (Machine Learning) — LLMs, AI Agents ve Machine Learning becerileri yapay zekâ alanını açıkça kapsıyor.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan listelenmiş.
- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **LLMs** (LLMs) — Profilde LLMs doğrudan listelenmiş.
- **GPT** (Azure OpenAI) — Azure OpenAI GPT modellerine erişim sağlayan servistir ve profilde listelenmiş.
- **Function Calling** (Tool Calling) — Tool Calling, function calling ile aynı kavramdır.
- **MCP** (MCP) — Profilde MCP doğrudan listelenmiş.
- **RAG** (RAG) — Profilde RAG doğrudan listelenmiş.
- **Embeddings** (Embedding Models) — Embedding Models profilde doğrudan listelenmiş.
- **Semantic Search** (Hybrid Search) — Hybrid Search, Vector Databases ve Embedding Models semantik aramayı kapsıyor.
- **Chunking** (Chunking) — Profilde Chunking doğrudan listelenmiş.
- **Citation** (Citations) — Profilde Citations doğrudan listelenmiş.
- **Prompt Engineering** (Prompt Engineering) — Profilde Prompt Engineering doğrudan listelenmiş.
- **LLM Evaluation** (Evals) — Evals ve LLMs birlikte LLM değerlendirme deneyimini gösteriyor.

## Kısmen

- **Google ADK** (AI Agents) — Agent geliştirme deneyimi var ama Google ADK'ya dair doğrudan bir madde yok.
- **CrewAI** (AI Agents) — Agent framework deneyimi (LangGraph) var ama CrewAI belirtilmemiş.
- **Type Hints** (Pydantic) — Pydantic ve TypeScript tip kullanımı ilgili ama Python type hints doğrudan belirtilmemiş.
- **Asyncio** (FastAPI) — FastAPI ve Python bilgisi asyncio'ya yakın ama doğrudan bir madde yok.
- **Gemini** (LLMs) — LLM deneyimi (Azure OpenAI) var ama Gemini belirtilmemiş.
- **Claude** (LLMs) — LLM deneyimi var ama Claude belirtilmemiş.
- **Multi-agent Systems** (AI Agents) — AI Agents ve LangGraph var ama multi-agent sistemi doğrudan belirtilmemiş.
- **Hub-and-Spoke Architecture** (AI Agents) — Agent orkestrasyonu temeli var ama bu mimari doğrudan belirtilmemiş.
- **Guardrails** (Prompt Engineering) — Prompt Engineering ve Structured Output ilgili ama guardrails doğrudan yok.
- **Grounding** (Citations) — RAG ve Citations ilgili ama grounding doğrudan belirtilmemiş.
- **LLM-as-Judge** (Evals) — Evals deneyimi var ama LLM-as-Judge yöntemi doğrudan belirtilmemiş.
- **Regression Testing** (Evals) — Evals ilgili ama regresyon testi doğrudan belirtilmemiş.

## Yok

- **uv** — Python paket yöneticisi uv ile ilgili bir beceri profilde yok.
- **Ruff** — Ruff ya da Python linter deneyimi profilde yok.
- **Pytest** — Test framework'ü olarak Pytest veya Python test becerisi profilde yok.

## Artı beceriler

_Yok._

## Çalışma planı

1. **[yüksek] Pytest** — Bu ilanda ajan ve API kodunun güvenilir çalıştığını otomatik testlerle kanıtlayabilmek temel bir beklentidir.
   - İlk adım: Pytest kurup mevcut bir Pydantic modelin doğrulama kuralları için 3 test fonksiyonu (geçerli, geçersiz, eksik alan) yaz ve çalıştır.
2. **[yüksek] uv** — İlandaki modern Python iş akışında bağımlılık ve sanal ortam yönetimi uv ile hızlı ve tekrarlanabilir şekilde yapılıyor.
   - İlk adım: uv kur, `uv init` ile boş bir proje aç, `uv add pytest fastapi` komutlarını çalıştırıp `uv run pytest` ile testi başlat.
3. **[yüksek] Ruff** — Ekip kod kalitesini ve tutarlı stili Ruff ile otomatik denetlediği için PR'larda temiz kod yazabilmek gerekir.
   - İlk adım: Mevcut bir projene `uv add --dev ruff` ile Ruff ekle, `ruff check` ve `ruff format` komutlarını çalıştırıp çıkan ilk 5 uyarıyı düzelt.
4. **[orta] Multi-agent Systems** — İlan birden fazla ajanın koordineli çalıştığı sistemler kurmayı hedefliyor ve tek ajan deneyimi bunun için yeterli değil.
   - İlk adım: İki ajanlı basit bir akış çiz ve kodla: biri araştırır, diğeri özetler; çıktıyı ikinciye aktar.
5. **[orta] Regression Testing** — Prompt veya model değiştiğinde ajan kalitesinin düşmediğini göstermek ilandaki değerlendirme sorumluluklarının parçasıdır.
   - İlk adım: Mevcut eval setinden 5 örneği Pytest testine çevir ve beklenen çıktılarla karşılaştıran bir referans (baseline) sonuç dosyası kaydet.
