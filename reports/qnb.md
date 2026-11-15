# AI Engineer / AI Agent Developer — QNB

**var: 20 · kısmen: 6 · yok: 1**

## Var

- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **LLM Agents** (AI Agents) — AI Agents ve LLMs becerileri LLM tabanlı ajanları doğrudan kapsıyor.
- **Agent Orchestration** (LangGraph) — LangGraph ajan orkestrasyonu için kullanılan bir çerçeve ve AI Agents ile birlikte bunu gösteriyor.
- **Tool Calling** (Tool Calling) — Profilde Tool Calling doğrudan var.
- **Function Calling** (Tool Calling) — Function calling ile tool calling aynı mekanizmayı ifade ediyor.
- **RAG** (RAG) — Profilde RAG doğrudan var.
- **MCP** (MCP) — Profilde MCP doğrudan listelenmiş.
- **Tool-use Design** (Tool Calling) — Tool Calling ve Context Engineering araç kullanım tasarımını kapsıyor.
- **API Integration** (REST APIs) — REST APIs ve SDK Integration API entegrasyonunu doğrudan gösteriyor.
- **Output Validation** (Pydantic) — Pydantic ve Structured Output çıktı doğrulamayı doğrudan kapsıyor.
- **Prompt Engineering** (Prompt Engineering) — Profilde Prompt Engineering doğrudan var.
- **Context Engineering** (Context Engineering) — Profilde Context Engineering doğrudan var.
- **LLM APIs** (Azure OpenAI) — Azure OpenAI ve LLMs LLM API kullanımını doğrudan gösteriyor.
- **LangChain** (LangChain) — Profilde LangChain doğrudan var.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan var.
- **Vector Databases** (Vector Databases) — Profilde Vector Databases ve Qdrant var.
- **Embedding Models** (Embedding Models) — Profilde Embedding Models doğrudan var.
- **REST APIs** (REST APIs) — Profilde REST APIs doğrudan var.
- **Microservices** (Microservices) — Profilde Microservices doğrudan var.
- **Software Engineering** (Git) — 4 yıl yazılım geliştirme deneyimi, Git ve CI/CD ile yazılım mühendisliği pratiği var.

## Kısmen

- **Multi-agent Workflows** (LangGraph) — AI Agents ve LangGraph temeli var ama çoklu ajan iş akışı açıkça belirtilmemiş.
- **Memory** (RAG) — RAG ve Context Engineering ilgili ama ajan hafızası doğrudan belirtilmemiş.
- **Guardrails** (Structured Output) — Structured Output ve Prompt Engineering ilgili ama guardrails doğrudan belirtilmemiş.
- **Fine-tuning** (Machine Learning) — Machine Learning temeli var ama LLM fine-tuning belirtilmemiş.
- **LlamaIndex** (LangChain) — LangChain benzer bir çerçeve, LlamaIndex'e geçiş kolay olur.
- **Langflow** (LangChain) — Langflow LangChain üzerine kurulu görsel araç, temel bilgi var.

## Yok

- **LoRA** — Profilde LoRA veya parametre-verimli ince ayar yok.

## Artı beceriler

- **Model Serving** → kısmen — FastAPI ile API sunma deneyimi var ama model serving doğrudan belirtilmemiş.
- **Self-hosted LLMs** → yok — Profilde kendi altyapısında LLM barındırma yok, sadece Azure OpenAI var.
- **Open-source LLMs** → kısmen — LLMs deneyimi var ama açık kaynak modeller doğrudan belirtilmemiş.
- **STT** → yok — Profilde konuşmadan metne dönüştürme ile ilgili beceri yok.
- **TTS** → yok — Profilde metinden konuşmaya dönüştürme ile ilgili beceri yok.
- **Voice-based Agents** → kısmen — AI Agents ve Streaming temeli var ama sesli ajan deneyimi yok.
- **English** → var — Profilde English (B2) listelenmiş.

## Çalışma planı

1. **[yüksek] LoRA** — İlan fine-tuning odaklı olduğu için LoRA gibi parametre-verimli yöntemleri bilmek büyük modelleri düşük maliyetle özelleştirmek açısından kritik.
   - İlk adım: Hugging Face PEFT ile küçük bir modele (ör. TinyLlama) 100 örneklik bir veri setiyle LoRA adaptörü eğiten bir Colab notebook'u çalıştır.
2. **[orta] Multi-agent Workflows** — İlan birden fazla ajanın birlikte çalıştığı iş akışları beklediği için LangGraph bilgini çoklu ajan koordinasyonuna taşıman gerekiyor.
   - İlk adım: LangGraph'ta bir araştırmacı ve bir yazar ajanını birbirine bağlayan 2 düğümlü bir graf kur.
3. **[orta] Memory** — Ajanların konuşmalar arasında bağlamı koruması ilanın temel gereksinimlerinden olduğu için RAG'in ötesinde kısa ve uzun süreli bellek yönetimi gerekiyor.
   - İlk adım: LangGraph'ta checkpointer kullanarak bir sohbet botuna oturumlar arası hafıza ekle.
4. **[orta] Guardrails** — Üretimdeki ajanların güvenli ve tutarlı çıktı vermesi gerektiği için structured output bilgini doğrulama ve güvenlik kurallarıyla genişletmelisin.
   - İlk adım: Mevcut bir structured output zincirine Pydantic doğrulaması ve konu dışı soruları reddeden basit bir kontrol ekle.
5. **[orta] Fine-tuning** — İlan LLM'leri kendi veriyle uyarlayabilen birini aradığı için mevcut ML temelini LLM fine-tuning sürecine bağlaman gerekiyor.
   - İlk adım: Hugging Face ile küçük bir sınıflandırma veri setinde bir modeli fine-tune eden resmi örnek notebook'u çalıştır.
