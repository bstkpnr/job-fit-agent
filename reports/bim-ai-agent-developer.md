# Yapay Zeka / AI Agent Geliştirici — BİM Birleşik Mağazalar A.Ş.

**var: 13 · kısmen: 12 · yok: 7**

## Var

- **Yapay Zeka** (AI Agents) — Profilde LLMs, AI Agents, RAG ve Machine Learning gibi birçok yapay zeka becerisi var.
- **Makine Öğrenmesi** (Machine Learning) — Profilde doğrudan Machine Learning becerisi var.
- **LangGraph** (LangGraph) — Profilde doğrudan LangGraph var.
- **Python** (Python) — Profilde doğrudan Python var.
- **LLM** (LLMs) — Profilde doğrudan LLMs var.
- **GPT** (Azure OpenAI) — Azure OpenAI GPT modellerine erişim sağlar ve profilde doğrudan listelenmiş.
- **Function Calling** (Tool Calling) — Tool Calling, Function Calling ile aynı kavramdır.
- **MCP** (MCP) — Profilde doğrudan MCP var.
- **RAG** (RAG) — Profilde doğrudan RAG var.
- **Embedding** (Embedding Models) — Profilde doğrudan Embedding Models var.
- **Vektör Arama** (Vector Databases) — Vector Databases, Qdrant ve Hybrid Search vektör aramayı kapsar.
- **Semantik Arama** (Hybrid Search) — Embedding Models, Qdrant ve Hybrid Search semantik aramayı doğrudan gösterir.
- **Prompt Engineering** (Prompt Engineering) — Profilde doğrudan Prompt Engineering var.

## Kısmen

- **Google ADK** (AI Agents) — Ajan geliştirme tecrübesi var ama Google ADK'ya dair doğrudan bir madde yok.
- **CrewAI** (LangGraph) — Ajan orkestrasyon çerçevesi LangGraph biliniyor, CrewAI doğrudan yok.
- **Type Hints** (Pydantic) — Pydantic ve TypeScript ile tip temelli çalışma var ama Python type hints doğrudan listelenmemiş.
- **asyncio** (Streaming) — Python ve FastAPI ile Streaming bilgisi var ama asyncio doğrudan belirtilmemiş.
- **Gemini** (LLMs) — LLM deneyimi var (Azure OpenAI) ama Gemini doğrudan yok.
- **Claude** (LLMs) — LLM deneyimi var ama Claude doğrudan listelenmemiş.
- **Multi-Agent Mimari** (AI Agents) — AI Agents ve LangGraph var ama çoklu ajan mimarisi açıkça belirtilmemiş.
- **Orkestratör Ajan** (LangGraph) — LangGraph ile ajan orkestrasyonu temeli var ama orkestratör ajan doğrudan belirtilmemiş.
- **Guardrail** (Structured Output) — Structured Output ve Prompt Engineering ilgili ama guardrail doğrudan yok.
- **Chunking** (RAG) — RAG çalışmasında chunking yaygındır ama profilde doğrudan belirtilmemiş.
- **Grounding** (RAG) — RAG grounding'e yakındır ama doğrudan grounding maddesi yok.
- **LLM Evaluation** (LLMs) — LLM deneyimi var ama değerlendirme çalışmasına dair doğrudan madde yok.

## Yok

- **uv** — Python paket yöneticisi uv ile ilgili bir madde yok.
- **ruff** — Ruff veya Python linter becerisi profilde yok.
- **pytest** — Test framework becerisi profilde yok.
- **Citation** — Kaynak gösterme (citation) ile ilgili doğrudan bir madde yok.
- **Eval Setleri** — Değerlendirme seti hazırlamaya dair bir madde yok.
- **LLM-as-Judge** — LLM-as-Judge yaklaşımına dair bir madde yok.
- **Regresyon Testleri** — Regresyon testi ile ilgili profilde bir madde yok.

## Artı beceriler

_Yok._

## Çalışma planı

1. **[yüksek] pytest** — Bu ilanda üretim kalitesinde Python kodu beklendiği için ajan ve RAG bileşenlerini otomatik testlerle doğrulayabilmek temel bir gerekliliktir.
   - İlk adım: pytest kurup mevcut bir projedeki tek bir fonksiyon için 3 test yaz (normal girdi, boş girdi, hatalı girdi) ve 'pytest -v' ile çalıştır.
2. **[yüksek] Eval Setleri** — LLM tabanlı sistemlerin kalitesi ancak sabit ve temsilci bir değerlendirme veri setiyle ölçülebildiği için ilan bu beceriyi merkezde tutuyor.
   - İlk adım: Kendi RAG veya ajan projen için 15 soru ve beklenen cevaptan oluşan bir eval.jsonl dosyası oluştur.
3. **[yüksek] LLM-as-Judge** — Serbest metin çıktılarını ölçeklenebilir şekilde puanlamak için LLM ile değerlendirme yapmak ilanın değerlendirme tarafında beklenen bir yöntemdir.
   - İlk adım: Bir LLM'e soru, cevap ve referans cevabı verip 1-5 arası puan ve tek cümlelik gerekçeyi JSON olarak döndüren 20 satırlık bir hakem prompt'u yaz, 5 örnekte dene.
4. **[yüksek] Regresyon Testleri** — Prompt veya model değiştiğinde mevcut kalitenin bozulmadığını güvenceye almak ilandaki sürdürülebilir LLM sistemleri geliştirme hedefinin parçasıdır.
   - İlk adım: Eval setindeki 10 örneği çalıştırıp skorları baseline.json dosyasına kaydet ve skor bu değerin altına düşerse başarısız olan bir pytest testi yaz.
5. **[yüksek] Citation** — RAG cevaplarının kaynaklarını göstermek, ilandaki güvenilir ve doğrulanabilir yanıt üretme beklentisini karşılar.
   - İlk adım: Mevcut RAG zincirinde her chunk'a kaynak ve sayfa metadata'sı ekle ve cevabın sonunda kullanılan kaynakları listeleyen bir çıktı üret.
