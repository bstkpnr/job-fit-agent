# AI Engineer / AI Agent Developer — QNB

**var: 18 · kısmen: 7 · yok: 2**

## Var

- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **LLM Agents** (AI Agents) — AI Agents ve LLMs becerileri LLM tabanlı ajanları doğrudan kapsıyor.
- **Tool Calling** (Tool Calling) — Profilde Tool Calling doğrudan var.
- **Function Calling** (Tool Calling) — Function calling ile tool calling aynı mekanizmayı ifade eder.
- **RAG** (RAG) — Profilde RAG doğrudan var.
- **Tool-Use Design** (Tool Calling) — Tool Calling ve Context Engineering araç kullanım tasarımını kapsıyor.
- **API Integration** (REST APIs) — REST APIs ve SDK Integration API entegrasyonunu doğrudan gösteriyor.
- **Output Validation** (Pydantic) — Pydantic ve Structured Output çıktı doğrulamayı doğrudan kapsıyor.
- **Prompt Engineering** (Prompt Engineering) — Profilde Prompt Engineering doğrudan var.
- **Context Engineering** (Context Engineering) — Profilde Context Engineering doğrudan var.
- **LLM APIs** (Azure OpenAI) — Azure OpenAI ve LLMs LLM API kullanımını doğrudan gösteriyor.
- **LangChain** (LangChain) — Profilde LangChain doğrudan var.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan var.
- **Vector Databases** (Vector Databases) — Profilde Vector Databases ve Qdrant doğrudan var.
- **Embedding Models** (Embedding Models) — Profilde Embedding Models doğrudan var.
- **REST APIs** (REST APIs) — Profilde REST APIs doğrudan var.
- **Microservices** (Microservices) — Profilde Microservices doğrudan var.
- **Software Engineering** (Git) — 4 yıllık yazılım geliştirme deneyimi ile Git, CI/CD gibi mühendislik pratikleri mevcut.

## Kısmen

- **Multi-Agent Workflows** (AI Agents) — AI Agents ve LangGraph temeli var ama çoklu ajan iş akışı doğrudan belirtilmemiş.
- **Agent Orchestration** (LangGraph) — LangGraph ajan orkestrasyonuna yakın ama doğrudan bir orkestrasyon maddesi yok.
- **Memory** (RAG) — RAG ilgili bir temel sağlıyor ama ajan hafızası doğrudan belirtilmemiş.
- **Guardrails** (Structured Output) — Structured Output ve Pydantic ilgili ama guardrails doğrudan belirtilmemiş.
- **Fine-Tuning** (Machine Learning) — Machine Learning temeli var ama fine-tuning deneyimi doğrudan belirtilmemiş.
- **LlamaIndex** (LangChain) — LangChain benzer bir çerçeve olduğundan öğrenmesi kolay ama LlamaIndex belirtilmemiş.
- **Langflow** (LangChain) — Langflow LangChain üzerine kurulu görsel araç, LangChain bilgisi öğrenmeyi kolaylaştırır.

## Yok

- **MCP** — Profilde Model Context Protocol ile ilgili doğrudan bir madde yok; Tool Calling MCP demek değildir.
- **LoRA** — Profilde LoRA ya da parametre verimli ince ayar ile ilgili madde yok.

## Çalışma planı

1. **[yüksek] MCP** — İlan, ajanların harici araç ve veri kaynaklarına standart bir protokolle bağlanmasını beklediği için MCP bilgisi doğrudan gereklidir.
   - İlk adım: Resmi MCP Python SDK'sını kurup tek bir araç (ör. verilen şehrin hava durumunu döndüren fonksiyon) sunan 30 satırlık yerel bir MCP sunucusu yaz ve bir istemciden çağır.
2. **[yüksek] LoRA** — İlan, büyük dil modellerini düşük maliyetle özelleştirebilen adayları aradığı için LoRA gibi parametre-verimli ince ayar yöntemleri kritik bir beceridir.
   - İlk adım: Hugging Face PEFT ile küçük bir modele (ör. 100-500 örnekli bir veri kümesi üzerinde) LoRA adaptörü ekleyen bir Colab not defteri aç ve eğitilebilir parametre sayısını yazdır.
3. **[orta] Multi-Agent Workflows** — İlan, birden fazla ajanın görev paylaşarak çalıştığı sistemler kurmayı gerektirdiği için tek ajan deneyimini çoklu ajan akışlarına genişletmek önemlidir.
   - İlk adım: Mevcut ajanını ikiye böl: biri araştırma yapan, diğeri sonucu özetleyen iki ajanı LangGraph'ta bağlayıp tek bir soruyla çalıştır.
4. **[orta] Agent Orchestration** — İlan, ajanların sırasını, koşullarını ve hata durumlarını yönetebilen orkestrasyon yetkinliği aradığı için LangGraph temelini ileri düzeye taşımak gerekir.
   - İlk adım: Mevcut bir LangGraph grafiğine koşullu bir kenar ekle: araç çağrısı başarısız olursa yeniden deneme düğümüne yönlendir.
5. **[orta] Memory** — İlan, oturumlar arasında bağlamı koruyan ajanlar beklediği için RAG'in ötesinde kısa ve uzun süreli bellek tasarımı bilmek önemlidir.
   - İlk adım: LangGraph'ta bir checkpointer ekleyerek aynı thread_id ile yapılan iki ayrı çağrıda ajanın önceki mesajı hatırladığını doğrula.
