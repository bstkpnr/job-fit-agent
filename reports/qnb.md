# AI Engineer / AI Agent Developer — QNB

**var: 12 · kısmen: 12 · yok: 5**

## Var

- **Python** (Python) — Profilde Python açıkça var.
- **LLM Agents** (AI Agents) — AI Agents, LLM tabanlı ajanları kapsar.
- **Tool Calling** (Tool Calling) — Profilde Tool Calling açıkça var.
- **Function Calling** (Tool Calling) — Function calling ile tool calling aynı mekanizmadır.
- **RAG** (RAG) — Profilde RAG açıkça var.
- **API Integration** (REST APIs) — REST API deneyimi API entegrasyonunu kapsar.
- **Database Integration** (SQL) — SQL veritabanı çalışmasını kapsar.
- **Prompt Engineering** (Prompt Engineering) — Profilde Prompt Engineering açıkça var.
- **LangGraph** (LangGraph) — Profilde LangGraph açıkça var.
- **Vector Databases** (Vector Databases) — Profilde Vector Databases açıkça var.
- **Embedding Models** (Embedding Models) — Profilde Embedding Models açıkça var.
- **REST APIs** (REST APIs) — Profilde REST APIs açıkça var.

## Kısmen

- **Multi-Agent Workflows** (AI Agents) — AI Agents ilgili ama çoklu ajan iş akışı deneyimi açıkça belirtilmemiş.
- **Agent Orchestration** (AI Agents) — Ajan deneyimi var ama orkestrasyon açıkça belirtilmemiş.
- **Memory Management** (Prompt Caching) — Prompt Caching bağlamla ilgili ama ajan hafıza yönetimi ile aynı değil.
- **Tool-Use Design** (Tool Calling) — Tool Calling kullanımı var ama araç tasarımı açıkça belirtilmemiş.
- **Multi-Agent Architectures** (AI Agents) — AI Agents ilgili ama çoklu ajan mimarisi belirtilmemiş.
- **Output Validation** (Structured Output) — Structured Output ilgili ama doğrulama açıkça belirtilmemiş.
- **Context Engineering** (Prompt Engineering) — Prompt Engineering yakın ama bağlam mühendisliği ile aynı değil.
- **LLM APIs** (LLMs) — LLM bilgisi var ama LLM API kullanımı açıkça belirtilmemiş.
- **LangChain** (LangGraph) — LangGraph bilen birinin LangChain öğrenmesi kolaydır.
- **LlamaIndex** (RAG) — RAG deneyimi LlamaIndex'e yakın ama araç belirtilmemiş.
- **Langflow** (LangGraph) — LangGraph ilgili ama Langflow görsel bir araçtır ve belirtilmemiş.
- **Software Engineering** (SDK Integration) — SDK Integration yazılım geliştirmeyle ilgili ama genel yazılım mühendisliğini kapsamaz.

## Yok

- **MCP** — Adaylardan hiçbiri Model Context Protocol ile ilgili değil.
- **Guardrails** — Adaylar arasında guardrail ile ilgili gerçek bir beceri yok.
- **Fine-Tuning** — Adaylar arasında model ince ayarı ile ilgili beceri yok.
- **LoRA** — Adaylardan hiçbiri LoRA ile ilgili değil.
- **Microservices** — Adaylar arasında mikroservis mimarisiyle ilgili beceri yok.

## Çalışma planı

1. **[yüksek] MCP** — Model Context Protocol, ilandaki ajanların araçlara ve veri kaynaklarına standart bir arayüzle bağlanması için aranan güncel bir protokoldür.
   - İlk adım: Resmi MCP Python SDK ile tek bir araç (ör. hava durumu sorgusu) sunan 30 satırlık bir MCP sunucusu yaz ve Claude Desktop'a bağla.
2. **[yüksek] Guardrails** — İlandaki üretim ortamındaki ajanların güvensiz, hatalı veya kapsam dışı çıktılar üretmesini engellemek için guardrail katmanı şarttır.
   - İlk adım: Guardrails AI veya NeMo Guardrails kurup bir sohbet botuna konu dışı soruları reddeden tek bir kural ekle.
3. **[yüksek] Fine-Tuning** — İlan, genel modellerin yetmediği alan özelinde modelleri özelleştirebilen adayları arıyor.
   - İlk adım: Hugging Face'te küçük bir modeli (ör. 100 örnekli bir sınıflandırma veri setiyle) ince ayar yapan hazır bir Colab not defterini çalıştır.
4. **[yüksek] LoRA** — LoRA, ilandaki ince ayar işlerini düşük maliyet ve sınırlı GPU ile yapılabilir kıldığı için vazgeçilmez bir tekniktir.
   - İlk adım: PEFT kütüphanesiyle küçük bir modele LoRA adaptörü ekleyip eğitilebilir parametre sayısını yazdıran 15 satırlık bir betik çalıştır.
5. **[yüksek] Microservices** — İlandaki yapay zekâ sistemlerinin ölçeklenebilir ve bağımsız dağıtılabilir servisler olarak çalışması mikroservis bilgisini gerektirir.
   - İlk adım: FastAPI ile bir LLM çağrısını sarmalayan tek endpoint'li bir servis yaz ve Docker konteyneri olarak çalıştır.
