# AI Mühendisi — Koç Üniversitesi

**var: 6 · kısmen: 15 · yok: 4**

## Var

- **Machine Learning** (Machine Learning) — Profilde Machine Learning doğrudan listelenmiş.
- **LLM** (LLMs) — Profilde LLMs doğrudan var.
- **RAG** (RAG) — Profilde RAG doğrudan var.
- **AI Agents** (AI Agents) — Profilde AI Agents doğrudan var.
- **Backend Integration** (REST APIs) — REST API, SDK entegrasyonu ve backend deneyimi profilde mevcut.
- **REST APIs** (REST APIs) — Profilde REST APIs doğrudan var.

## Kısmen

- **Data Science** (Machine Learning) — ML ve tahmine dayalı modelleme var ama kapsamlı veri bilimi deneyimini gösteren madde yok.
- **Classification** (Machine Learning) — Genel ML bilgisi var ama sınıflandırmayı doğrudan gösteren madde yok.
- **Regression** (Predictive Modeling) — Tahmine dayalı modelleme ilgili ama regresyon açıkça belirtilmemiş.
- **Clustering** (Machine Learning) — Genel ML temeli var ama kümeleme doğrudan görünmüyor.
- **Anomaly Detection** (Machine Learning) — ML temeli var ama anomali tespiti doğrudan belirtilmemiş.
- **Forecasting** (Predictive Modeling) — Tahmine dayalı modelleme ilgili ama zaman serisi tahmini açık değil.
- **Data Analysis** (Predictive Modeling) — Modelleme deneyimi var ama doğrudan veri analizi maddesi yok.
- **Feature Engineering** (Machine Learning) — ML temeli var ama özellik mühendisliği açıkça görünmüyor.
- **Model Training** (Machine Learning) — ML ve tahmine dayalı modelleme var ama model eğitimi doğrudan belirtilmemiş.
- **Model Selection** (Machine Learning) — ML temeli var ama model seçimi doğrudan gösterilmemiş.
- **Train/Test Split** (Machine Learning) — ML bilgisi bunu ima edebilir ama doğrudan madde yok.
- **Cross Validation** (Machine Learning) — ML temeli var ama çapraz doğrulama doğrudan belirtilmemiş.
- **Hyperparameter Tuning** (Machine Learning) — ML temeli var ama hiperparametre ayarı doğrudan görünmüyor.
- **Model Evaluation** (Evals) — Evals (LLM değerlendirme) ilgili ama klasik ML model değerlendirmesi değil.
- **Overfitting** (Machine Learning) — ML temeli var ama aşırı öğrenme konusu doğrudan belirtilmemiş.

## Yok

- **Data Cleaning** — Profilde veri temizleme ile ilgili bir madde yok.
- **Data Leakage** — Profilde veri sızıntısıyla ilgili bir madde yok.
- **Class Imbalance** — Profilde sınıf dengesizliğiyle ilgili bir madde yok.
- **Data Quality** — Profilde veri kalitesine yönelik doğrudan bir madde yok.

## Artı beceriler

_Yok._

## Çalışma planı

1. **[yüksek] Data Cleaning** — Tahmine dayalı modellerin kalitesi doğrudan temizlenmiş veriye bağlı olduğu için bu ilanda veri hazırlama günlük işin büyük bir parçasıdır.
   - İlk adım: Kaggle'dan eksik değer ve tekrar eden satır içeren küçük bir CSV indir, pandas ile eksikleri doldur, kopyaları sil ve önce/sonra satır sayısını yazdır.
2. **[yüksek] Data Leakage** — Veri sızıntısı model performansını gerçekte olduğundan iyi gösterdiği için ilandaki model değerlendirme ve seçim sorumluluklarında kritik bir hatadır.
   - İlk adım: Ölçekleme işlemini train/test ayrımından önce yapan bir scikit-learn kodu yaz, sonra aynısını Pipeline ile düzelt ve iki skoru karşılaştır.
3. **[yüksek] Class Imbalance** — Sınıflandırma ve anomali tespiti gibi ilan görevlerinde dengesiz veri yaygındır ve accuracy tek başına yanıltıcı sonuç verir.
   - İlk adım: Kredi kartı sahtekarlığı gibi dengesiz bir veri setinde class_weight='balanced' ile ve bu ayar olmadan lojistik regresyon eğit, precision/recall farkını karşılaştır.
4. **[yüksek] Data Quality** — Veri kalitesi sorunlarını erken yakalamak, ilandaki analiz ve modelleme çıktılarının güvenilir olmasını sağlar.
   - İlk adım: Seçtiğin bir veri seti için eksik oran, benzersiz değer sayısı ve aykırı değer kontrollerini yapan 15 satırlık bir pandas raporu fonksiyonu yaz.
5. **[orta] Model Evaluation** — Modellerin doğru metriklerle değerlendirilmesi ilandaki model seçimi ve iyileştirme işlerinin temelidir.
   - İlk adım: Bir sınıflandırma modeli için scikit-learn ile confusion matrix, precision, recall ve F1 değerlerini yazdıran bir kod çalıştır.
