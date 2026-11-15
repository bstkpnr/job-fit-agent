# AI Mühendisi — Koç Üniversitesi

**var: 7 · kısmen: 18 · yok: 2**

## Var

- **Büyük Dil Modelleri** (LLMs) — Profilde LLMs doğrudan listelenmiş.
- **RAG** (RAG) — Profilde RAG doğrudan mevcut.
- **Akıllı Ajan Sistemleri** (AI Agents) — AI Agents becerisi akıllı ajan sistemlerini doğrudan kapsıyor.
- **Machine Learning** (Machine Learning) — Profilde Machine Learning doğrudan mevcut.
- **Tahminleme** (Predictive Modeling) — Predictive Modeling tahminleme becerisini doğrudan kapsıyor.
- **Backend Entegrasyonu** (REST APIs) — REST APIs, Node.js ve FastAPI deneyimi backend entegrasyonunu gösteriyor.
- **API Servisleri** (REST APIs) — REST APIs ve FastAPI ile API servisi geliştirme deneyimi var.

## Kısmen

- **Data Science** (Machine Learning) — ML ve SQL temeli var ancak veri bilimi iş akışını gösteren doğrudan bir madde yok.
- **Sınıflandırma** (Machine Learning) — ML temeli var ama sınıflandırmaya özgü bir beceri belirtilmemiş.
- **Regresyon** (Predictive Modeling) — Tahminsel modelleme ilgili ama regresyon açıkça belirtilmemiş.
- **Clustering** (Machine Learning) — ML temeli var ancak kümeleme açıkça yok.
- **Anomaly Detection** (Machine Learning) — ML temeli var ancak anomali tespiti açıkça yok.
- **Veri Analizi** (SQL) — SQL ile veri sorgulama var ama analiz becerisi doğrudan belirtilmemiş.
- **Feature Engineering** (Machine Learning) — ML temeli var ama özellik mühendisliği açıkça belirtilmemiş.
- **Model Eğitimi** (Machine Learning) — ML deneyimi var ancak model eğitimi doğrudan gösterilmemiş.
- **Model Seçimi** (Predictive Modeling) — Modelleme temeli var ama model seçimi açıkça belirtilmemiş.
- **Model Karşılaştırma** (Predictive Modeling) — Modelleme temeli var ama model karşılaştırma doğrudan yok.
- **Train/Test Split** (Machine Learning) — ML temelinin parçası olabilir ama profilde açıkça yer almıyor.
- **Cross Validation** (Machine Learning) — ML temeli var ancak çapraz doğrulama açıkça belirtilmemiş.
- **Hyperparameter Tuning** (Machine Learning) — ML temeli var ama hiperparametre ayarı doğrudan gösterilmemiş.
- **Model Değerlendirme** (Predictive Modeling) — Modelleme deneyimi ilgili ama değerlendirme becerisi açıkça yok.
- **Overfitting** (Machine Learning) — ML temeli var ama aşırı öğrenme konusu profilde belirtilmemiş.
- **Data Leakage** (Machine Learning) — ML temeli var ancak veri sızıntısı doğrudan belirtilmemiş.
- **Class Imbalance** (Machine Learning) — ML temeli var ama sınıf dengesizliği açıkça belirtilmemiş.
- **Üretim Ortamı AI Servisleri** (FastAPI) — AI, FastAPI ve Microservices var ama üretim ortamı deneyimi doğrudan belirtilmemiş.

## Yok

- **Veri Temizleme** — Profilde veri temizleme ile ilgili bir beceri yok.
- **Veri Kalitesi** — Profilde veri kalitesiyle ilgili bir beceri yok.

## Artı beceriler

_Yok._

## Çalışma planı

1. **[yüksek] Veri Temizleme** — İlanda model başarısı büyük ölçüde ham verinin temizlenmesine bağlı olduğu için bu beceri eksik olursa diğer tüm ML adımları zayıf kalır.
   - İlk adım: Kaggle'dan eksik değer ve tekrar eden satır içeren küçük bir CSV indir, pandas ile eksik değerleri doldur, tekrarları sil ve aykırı değerleri işaretleyen 30 satırlık bir script yaz.
2. **[yüksek] Veri Kalitesi** — Güvenilir modeller için verinin doğruluk, tutarlılık ve eksiksizlik açısından ölçülmesi ve izlenmesi ilanın temel beklentilerinden biridir.
   - İlk adım: Elindeki bir veri setinde eksik oran, benzersizlik ve değer aralığı kontrollerini yapan 5 kurallık bir veri kalitesi raporu (pandas ile) oluştur.
3. **[orta] Data Leakage** — Veri sızıntısı modelin gerçek performansını olduğundan iyi gösterdiği için ilandaki model değerlendirme sorumluluğunda kritik bir risktir.
   - İlk adım: Scaler'ı train/test ayrımından önce fit ettiğin bir örnek yaz, sonra aynısını Pipeline ile düzeltip iki skor arasındaki farkı karşılaştır.
4. **[orta] Üretim Ortamı AI Servisleri** — İlan modellerin sadece eğitilmesini değil üretimde servis olarak çalıştırılmasını da beklediği için FastAPI bilgisini bu yönde genişletmek gerekir.
   - İlk adım: Eğitilmiş bir scikit-learn modelini joblib ile kaydet ve FastAPI'de /predict endpoint'i olarak sun.
5. **[orta] Model Değerlendirme** — İlanda farklı modellerin doğru metriklerle değerlendirilip karşılaştırılması beklendiği için metrik seçimi güçlü olmalıdır.
   - İlk adım: Bir sınıflandırma modeli için accuracy, precision, recall, F1 ve ROC-AUC değerlerini tek bir sklearn script'inde hesapla.
