# AI Engineer / AI Agent Developer — QNB

**var: 20 · kısmen: 6 · yok: 1**

## Var

- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **LLM Applications** (LLMs) — LLMs, RAG, AI Agents ve Azure OpenAI ile LLM uygulamaları geliştirme deneyimi var.
- **AI Agents** (AI Agents) — Profilde AI Agents doğrudan var.
- **Tool Calling** (Tool Calling) — Profilde Tool Calling doğrudan var.
- **RAG** (RAG) — Profilde RAG doğrudan var.
- **Model Context Protocol** (MCP) — MCP profilde doğrudan listelenmiş.
- **System Integration** (SDK Integration) — SDK Integration, REST APIs ve Payment Systems entegrasyon deneyimini gösteriyor.
- **APIs** (REST APIs) — REST APIs, FastAPI ve Express ile API geliştirme deneyimi var.
- **Databases** (SQL) — SQL, Firebase ve Vector Databases ile veritabanı deneyimi var.
- **Output Validation** (Pydantic) — Pydantic ve Structured Output çıktı doğrulamayı doğrudan kapsar.
- **Prompt Engineering** (Prompt Engineering) — Profilde Prompt Engineering doğrudan var.
- **Context Engineering** (Context Engineering) — Profilde Context Engineering doğrudan var.
- **LLM APIs** (Azure OpenAI) — Azure OpenAI ve LLMs ile LLM API kullanımı doğrudan var.
- **LangChain** (LangChain) — Profilde LangChain doğrudan var.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan var.
- **Vector Databases** (Vector Databases) — Profilde Vector Databases ve Qdrant var.
- **Embedding Models** (Embedding Models) — Profilde Embedding Models doğrudan var.
- **REST APIs** (REST APIs) — Profilde REST APIs doğrudan var.
- **Microservices** (Microservices) — Profilde Microservices doğrudan var.
- **Software Engineering** (Git) — 4 yıl yazılım geliştirme deneyimi, Git ve CI/CD pratikleri var.

## Kısmen

- **Multi-agent Systems** (AI Agents) — AI Agents ve LangGraph var ama çoklu ajan sistemi doğrudan belirtilmemiş.
- **Agent Orchestration** (LangGraph) — LangGraph ajan orkestrasyonu için ilgili bir temel sağlar ama doğrudan belirtilmemiş.
- **Guardrails** (Structured Output) — Structured Output ve Pydantic ilgili ama guardrails doğrudan belirtilmemiş.
- **Fine-tuning** (Machine Learning) — Machine Learning ilgili bir temel ama fine-tuning deneyimi belirtilmemiş.
- **LlamaIndex** (LangChain) — LangChain benzer bir çerçeve olup öğrenmesi kolay olur ama LlamaIndex belirtilmemiş.
- **Langflow** (LangChain) — LangChain ekosistemine aşinalık var ama Langflow doğrudan belirtilmemiş.

## Yok

- **LoRA** — Profilde LoRA veya parametre-verimli ince ayar deneyimi yok.

## Artı beceriler

- **Model Serving** → kısmen — FastAPI ile servis sunma temeli var ama model serving doğrudan belirtilmemiş.
- **Open-source LLMs** → yok — Profilde açık kaynak LLM deneyimini gösteren bir madde yok.
- **Self-hosted LLMs** → yok — Kendi altyapısında LLM barındırma deneyimi belirtilmemiş.
- **Speech-to-Text** → yok — Profilde konuşmadan metne dönüştürme deneyimi yok.
- **Text-to-Speech** → yok — Profilde metinden konuşmaya dönüştürme deneyimi yok.
- **Voice Agents** → kısmen — AI Agents deneyimi var ama sesli ajan deneyimi belirtilmemiş.

## Çalışma planı

1. **[yüksek] LoRA** — İlan parametre-verimli ince ayar bilgisi istiyor ve adayın bu konuda hiç deneyimi olmadığı için en büyük açık burada.
   - İlk adım: Hugging Face PEFT ile küçük bir modele (ör. TinyLlama) 100 örneklik bir veri setiyle LoRA adaptörü eğiten bir Colab not defteri çalıştır.
2. **[orta] Multi-agent Systems** — İlan birden fazla ajanın birlikte çalıştığı sistemler istiyor ve adayın tek ajan deneyimini bu seviyeye taşıması gerekiyor.
   - İlk adım: Bir araştırmacı ve bir yazar ajanı birbirine mesaj geçirecek şekilde 30 satırlık bir örnek yaz.
3. **[orta] Agent Orchestration** — Birden fazla ajanın ve aracın akışını yönetmek ilandaki ajan tabanlı sistemlerin temelini oluşturuyor.
   - İlk adım: LangGraph'ta koşullu kenarı olan 3 düğümlü bir grafik (yönlendirici, araç, yanıt) kur.
4. **[orta] Guardrails** — Üretimdeki LLM çıktılarının güvenli ve doğrulanmış olması ilan için kritik ve adayın yapılandırılmış çıktı bilgisi buna iyi bir temel.
   - İlk adım: Mevcut structured output örneğine Pydantic doğrulaması ve geçersiz çıktıda yeniden deneme ekle.
5. **[orta] Fine-tuning** — İlan model ince ayarı yetkinliği arıyor ve adayın makine öğrenmesi temeli bu konuya geçişi kolaylaştırıyor.
   - İlk adım: Hugging Face'te küçük bir sınıflandırma modelini 200 örnekle ince ayarla ve önce/sonra doğruluğunu karşılaştır.
