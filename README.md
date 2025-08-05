<div style="text-align: start; margin-bottom: 4px;">
    <h1><b>Bank Marketing Campaign</h1>
    <h4><b>Final Project</b><br>JCDSOL-18<br>by : Akmal Raafid Taufiqurrahman & Rikal Muhammad</h4>
</div>
---
## **Contents:**

1. Dataset Overview

2. Problem Statement
3. Data Understanding
4. Exploratory Data Analysis
5. Preprocessing
6. Methodology (Modeling/Analysis)
7. Conclusion and Recommendation
   ---
## **Dataset Overview**
#### **Konteks Dataset**
Data yang digunakan dalam proyek ini berasal dari kampanye pemasaran langsung sebuah bank di **Portugal**, yang bertujuan untuk menawarkan produk deposito berjangka (term deposit) kepada nasabah. Dataset ini berisi informasi mengenai interaksi telemarketing yang dilakukan oleh agen bank kepada berbagai segmen nasabah, serta hasil akhir dari setiap kontak: apakah nasabah bersedia membuka deposito atau tidak.

Dataset terdiri dari 41.188 baris data dan 21 kolom, mencakup informasi sebagai berikut:

- Atribut Sosial-Ekonomi Nasabah<br><br>Contoh: age, job, marital, education, default, housing, loan<br><br>
- Detail Kampanye Pemasaran<br><br>Contoh: contact (jenis kontak), month, day_of_week, duration, campaign (jumlah kontak selama kampanye), pdays, previous, poutcome (hasil kampanye sebelumnya)<br><br>
- Indikator Ekonomi Makro saat Kampanye<br><br>Contoh: emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed<br><br>
- Target (Label)<br>y: Apakah nasabah membuka deposito berjangka (yes atau no)


Data ini telah digunakan secara luas dalam berbagai studi dan kompetisi data science, termasuk dalam publikasi Moro, Cortez & Rita (2014) yang menjadi referensi utama untuk pendekatan berbasis data dalam pengambilan keputusan pemasaran di industri perbankan.

#### **Sumber Statement**
Semua pernyataan berikut didasarkan pada dataset kampanye pemasaran bank Portugis yang digunakan dalam studi **Moro et al. (2014)**.
<br>Data ini dikumpulkan antara **Mei 2008 hingga November 2010**, mencakup **41.188 interaksi**, dan sesuai dengan yang tersedia di Kaggle (https://www.kaggle.com/code/janiobachmann/bank-marketing-campaign-opening-a-term-deposit?scriptVersionId=11675860) ataupun UCI Repository (https://archive.ics.uci.edu/dataset/222/bank+marketing).

Daftar sumber Refensi juga akan kami tuliskan pada akhir content.

---
## **Problem Statement**
#### **Latar Belakang Masalah**

Portugal diperkirakan memiliki `10,75 Juta` penduduk per tahun 2024 dengan kepadatan penduduk sekitar 116,6 jiwa per kilometer persegi, lebih tinggi dibandingkan dengan kebanyakan negara di uni eropa, dan sedikit melampaui rata-rata Uni Eropa sebesar 105,4 jiwa per kilometer persegi (273/mil persegi). Wilayah yang paling padat penduduknya adalah wilayah metropolitan Lisbon (yang berisi lebih dari seperempat populasi negara tersebut), wilayah metropolitan Porto dan pesisir Atlantik, sementara wilayah luas lainnya sangat jarang penduduknya. Jumlah penduduk negara ini hampir berlipat ganda selama abad ke-20, tetapi pola pertumbuhannya sangat tidak merata karena migrasi internal berskala besar dari pedesaan Utara ke kota-kota industri Lisbon dan Porto

Dalam beberapa tahun terakhir, kondisi keuangan rumah tangga di Portugal menunjukkan tren yang positif, menciptakan peluang strategis bagi sektor perbankan untuk mengembangkan pendekatan pemasaran berbasis data. Berdasarkan analisis dari Corum Investments Portugal dan BA&N Research Unit, lebih dari 21% kekayaan bersih rumah tangga di Portugal saat ini disimpan dalam bentuk simpanan bank—menjadi proporsi tertinggi di kawasan euro. Hal ini mencerminkan preferensi masyarakat terhadap produk tabungan yang konservatif dan berisiko rendah.

Setiap orang Portugal memiliki rata-rata €22.300 dalam bentuk simpanan bank (deposito dan tabungan), berdasarkan data ECB per Q1 2024 dengan jumlah total simpanan berjangka di bank untuk nasabah perorangan sekitar €100,704 miliar. Selama empat kuartal berturut-turut, pendapatan 'disposabel' rumah tangga terus mengalami pertumbuhan, mencapai hampir €189 miliar pada pertengahan 2024, dengan tingkat pertumbuhan tahunan sebesar 7,9%. Sementara pengeluaran konsumsi hanya tumbuh sebesar 4,6%, menyisakan ruang tabungan yang signifikan, yaitu sekitar €19 miliar. Kondisi ini menunjukkan bahwa kemampuan dan kecenderungan masyarakat untuk menabung meningkat, menciptakan peluang bagi bank untuk menawarkan produk-produk finansial yang lebih kompetitif dan tersegmentasi. 

Namun demikian, tingginya alokasi dana dalam bentuk simpanan tradisional juga menandakan rendahnya eksposur terhadap instrumen investasi seperti saham, obligasi, dan reksa dana. Misalnya, investasi rata-rata dalam saham hanya sebesar €590 (0,6% dari kekayaan bersih), sementara investasi dalam reksa dana sebesar €2.720 (2,6%). Selain itu, melalui analisis ini juga mengungkap bahwa tingginya preferensi terhadap simpanan konvensional membawa dampak berupa rendahnya imbal hasil, terutama ketika suku bunga bank sentral mengalami penurunan. Imbal hasil deposito berjangka tahunan pada periode terbaru tercatat hanya sebesar 2,3% secara bruto, tidak cukup untuk mengimbangi inflasi. [https://en.wikipedia.org/wiki/Demographics_of_Portugal, https://www.aman-alliance.org/Home/ContentDetail/84837]

Karena tidak ada data langsung mengenai jumlah individu yang melakukan deposito berjangka, kita hanya bisa memperkirakan secara kasar seperti berikut:

- Total simpanan berjangka: €100,704 miliar
- Rata-rata simpanan per orang: €22.300
- Perkiraan jumlah deposan = Total term deposit / Rata-rata simpanan per orang = €100.704 miliar / €22.300 ≈ 4,52 juta orang

Ini berarti sekitar 42 % dari penduduk Portugal yang menyimpan di term deposit. Hal ini mengindikasikan bahwa term deposit memiliki market yang begitu besar sehingga menjadikan bank memiliki potensi yang lebih besar untuk mendapatkan term deposit (deposito berjangka) yang dapat memberikan stabilitas dana, sumber pendanaan, dan dukungan terhadap kegiatan kredit.

Dalam konteks ini, sebuah bank di Portugal menjalankan beberapa kampanye pemasaran melalui panggilan telepon (telemarketing) dengan tujuan utama untuk mempromosikan produk deposito berjangka (term deposit) kepada nasabah dan calon nasabah. Kampanye ini dilakukan dalam berbagai periode, dengan strategi pemasaran langsung yang sangat bergantung pada interaksi personal via telepon. Telemarketing dilakukan untuk menarik, melibatkan dan mempertahankan nasabah dengan mempromosikan produk bank (term deposit) serta membangun hubungan jangka panjang yang kuat sehingga mendukung dan menstabilkan keuangan bank. Pada dataset ini, Hasil dari kampanye ini berupa data personal, ekonomi serta deskripsi kampanye yang telah dilakukan terhadap nasabah. Ketika nasabah setuju untuk melakukan deposit, target variabel 'y' akan diberi tanda `yes`, sebaliknya `no`.

---
#### **Masalah**

Produk deposito berjangka (term deposit) merupakan salah satu sumber pendanaan utama bagi industri perbankan. Menurut data dari European Central Bank (ECB), deposito dengan jangka waktu tetap memberi bank fleksibilitas likuiditas lebih tinggi karena dananya tidak dapat ditarik sewaktu-waktu, menjadikannya lebih stabil dibandingkan tabungan biasa. Hal ini menjadikan peningkatan penjualan deposito sebagai prioritas strategis dalam pengelolaan dana bank (https://data.ecb.europa.eu).

Dataset yang digunakan dalam proyek ini berasal dari kampanye pemasaran langsung sebuah bank di Portugal yang dilakukan melalui telemarketing antara Mei 2008 hingga November 2010, dan telah dianalisis dalam publikasi ilmiah oleh Moro et al. (2014). Dalam periode tersebut, terdapat 41.188 interaksi telepon yang direkam, namun hanya sekitar 3.924 pelanggan (8,8%) yang akhirnya membuka deposito berjangka (https://archive.ics.uci.edu/ml/datasets/Bank+Marketing; Moro et al., 2014).

Sebagai ilustrasi berbasis data: jika bank menghubungi 1.000 calon pelanggan, maka rata-rata hanya sekitar 88 pelanggan yang berhasil dikonversi menjadi pembuka deposito.
Berdasarkan laporan statistik dari Banco de Portugal, rata-rata saldo deposito berjangka individu (retail term deposit) selama periode 2008–2010 berada pada kisaran €4.500 hingga €6.000 per nasabah. Oleh karena itu, angka €5.000 digunakan dalam proyek ini sebagai estimasi konservatif dan berbasis data (https://www.bportugal.pt/en/page/statistics).

Dengan demikian, peningkatan efektivitas kampanye sebesar hanya 2 poin persentase—misalnya dari 8,8% menjadi 10,8%—dapat menambah sekitar 20 nasabah baru dari setiap 1.000 kontak. Dengan nominal deposito rata-rata €5.000 per pelanggan, maka potensi tambahan dana terhimpun adalah €100.000, hanya dari satu batch kampanye.

Masalah utama yang ingin diselesaikan adalah:

Bagaimana bank dapat mengidentifikasi strategi kampanye yang paling berdampak terhadap keputusan nasabah untuk membuka deposito berjangka, sehingga pendekatan pemasaran menjadi lebih efisien dan menghasilkan peningkatan konversi yang signifikan secara finansial?

---
#### **Tujuan**

Proyek ini dibangun di atas dua landasan utama: analisis eksploratif untuk memahami pola dalam data, dan pengembangan model prediktif untuk pengambilan keputusan yang presisi.

1. **Analytical Objective: Business Insight Generation**
<br><br>Tujuan pertama adalah mengeksplorasi dataset secara menyeluruh untuk menemukan:
    - Faktor-faktor utama yang memengaruhi keberhasilan kampanye, seperti durasi kontak, waktu pelaksanaan, dan karakteristik nasabah.
    - Pola-pola interaksi yang efektif maupun kontra-produktif (misal kampanye terlalu sering).
    - Rekomendasi praktis bagi tim marketing untuk meningkatkan efisiensi kontak dan alokasi sumber daya secara tepat sasaran.

2. **Predictive Objective: Machine Learning Application**
<br><br>Tujuan dari proyek ini adalah membangun model machine learning untuk membantu bank menentukan apakah seorang pelanggan akan melakukan term deposit, berdasarkan informasi yang tersedia **hingga saat ini**.

    Dataset yang digunakan merepresentasikan hasil dari interaksi telemarketing terakhir terhadap masing-masing pelanggan. Masing-masing baris dianggap mewakili **satu pelanggan unik**, tanpa riwayat kontak terpisah per individu.

    **Model tidak terbatas hanya untuk prediksi kontak pertama**

    Meskipun fitur seperti `campaign` menunjukkan jumlah total kontak yang sudah dilakukan terhadap seorang pelanggan, informasi ini justru merefleksikan **kondisi nyata saat ini** misalnya, "ini adalah kontak ke-2 atau ke-4 untuk pelanggan A." Karena itu:

    - Model **tidak hanya memprediksi pada kontak pertama**
    - Tapi juga memprediksi hasil kontak **saat ini**, terlepas dari sudah ke berapa kali pelanggan dihubungi

    **Justifikasi Pendekatan Ini:**

    - **Tidak ada ID pelanggan** → kita tidak bisa membedakan riwayat per orang
    - **Tidak ada baris eksplisit untuk tiap urutan kontak** → dataset hanya menyimpan snapshot terakhir per pelanggan
    - Maka, **satu baris = satu pelanggan** adalah asumsi paling aman dan praktis
    - Fitur `campaign`, `previous`, dan `poutcome` tetap bisa digunakan karena nilainya sudah tersedia **sebelum prediksi dilakukan**

    **Tujuan kedua adalah membangun model prediktif berbasis machine learning yang mampu:**

    > Memprediksi apakah pelanggan akan melakukan term deposit pada saat mereka dihubungi, dengan mempertimbangkan informasi historis dan status saat ini tanpa menggunakan data masa depan seperti `duration`.

    Model ini akan digunakan untuk:
    - Membantu tim marketing memprioritaskan pelanggan yang paling potensial
    - Mengurangi biaya kampanye dengan menyaring pelanggan yang kemungkinan besar tidak tertarik

Dengan pendekatan ini, bank diharapkan tidak hanya mendapatkan insight retrospektif, tetapi juga kemampuan untuk mengoptimalkan keputusan kampanye secara proaktif ke depannya.

---
#### **Pendekatan Analisis**

Kami akan menganalisis karakteristik nasabah terlebih dahulu melalui data yang ada untuk mengetahui nasabah mana yang berminat untuk melakukan term deposit serta menganalisis faktor-faktor apa saja yang mempengaruhi keputusan nasabah untuk melakukan term deposit. Setelah itu, kami akan membuat model prediksi berdasarkan fitur yang ada untuk mengetahui probabilitas nasabah melakukan term deposit.

---
#### **Pendekatan Metriks**

Apabila dilihat dari dataset yang ada terdapat variabel y (target) yang menunjukan sebagai berikut:

Target:

`0 : Nasabah tidak melakukan term deposit`

`1 : Nasabah melakukan term deposit`

`Type 0 Error: Nasabah yang diprediksi tidak melakukan term deposit tetapi pada faktanya nasabah ini melakukan term deposit (False Negative)` -> Konsekuensi: kehilangan nasabah potensial

`Type 1 Error: Nasabah yang diprediksi melakukan term deposit tetapi pada faktanya nasabah ini tidak melakukan term deposit (False Positive)` -> Konsekuensi: Pengeluaran biaya yang tidak tepat sasaran

**Business Metric:**

- Berdasarkan [LiveAgent](https://www.liveagent.com/customer-support-glossary/cost-per-call/), biaya panggilan telepon di portugal adalah 2.34 Euro - 4.85 Euro. Kita asumsikan bahwa cost dari tiap panggilan adalah 3.6 Euro.
- Berdasarkan data dari [Institut Statistik Portugal](https://www.ine.pt/xportal/xmain?PUBLICACOESmodo=2&PUBLICACOESpub_boui=141619793&xpgid=ine_publicacoes&xpid=INE), pada tahun 2010 pendapatan rata rata penduduk per tahunnya adalah 23,811 Euro dengan pengeluaran untuk biaya hidup sebesar 20,391 Euro yang menyisakan disposable income sebesar 3,420 Euro.
- Berdasarkan [Banco De Portugal](https://www.bportugal.pt/sites/default/files/anexos/papers/ab201014_e.pdf), rata rata orang akan menginvestasikan sekitar `2,695 Euro`.
- Berdasarkan [Banco De Portugal](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/ref_november10_e.pdf), Bunga pinjaman berada di kisaran 4.2 – 5.1% tergantung dari jangka waktu dan menurut [TradingEconomics](https://tradingeconomics.com/portugal/bank-lending-rate#:~:text=Bank%20Lending%20Rate%20in%20Portugal,source%3A%20European%20Central%20Bank) rata rata lending interest rate di portugal dari tahun 2003-2025 adalah 4.98%. 
- Berdasarkan [TheBanks](https://thebanks.eu/compare-banking-products/time-deposit-accounts/Portugal), deposit interest rate portugal berkisar antara 0.10% - 3% tergantung dari jangka waktunya. Apabila dilihat dari minimal depositonya, kita dapat menyimpulkan bahwa term deposit yang sesuai dengan kriteria yang ada adalah 0.10%

Maka dari itu, dapat disimpulkan bahwa:

Rata-rata investasi:
- `2695 Euro`

Keuntungan per nasabah (Kelas 1):
- `Nominal deposit * (Bunga Pinjaman - Bunga deposit)` -> `2695 * (4.98%-0.10%) = 131 Euro per tahun`

Potensi Keuntungan(berdasarkan jumlah nasabah yang ada pada dataset):
- `131 Euro * 41188 = 5,395,628 Euro` -> apabila semua nasabah melakukan term deposit

Kerugian:
- Type 0 Error -> Apabila kehilangan nasabah yang akan mendepositkan uang sejumlah `2695 Euro`, maka bank akan mendapat kerugian sebesar `131 Euro` dari tiap nasabah yang hilang.
- Type 1 Error -> Apabila bank mengeluarkan biaya untuk nasabah yang tidak melakukan term deposit, maka bank akan mengeluarkan biaya untuk setiap panggilannya. Kita asumsikan jumlah panggilan rata rata per nasabah adalah 5x panggilan berdasarkan data, maka untuk setiap panggilan yang tidak terkonversi, bank akan merugi sekitar `18 Euro` 
---
## **Data Understanding**

### Attribute Information

| Attribute | Data Type | Description |
| --- | --- | --- |
| age | Integer | Usia calon nasabah |
| job | String | Pekerjaan calon nasabah |
| marital | String | Status pernikahan calon nasabah |
| education | String | Status pendidikan calon nasabah |
| default | String | Pernahkah calon nasabah gagal bayar sebelumnya? |
| housing | String | Apakah calon nasabah memiliki cicilan rumah? |
| loan | String | Apakah calon nasabah memiliki pinjaman? |
| contact | String | Jenis komunikasi yang digunakan |
| month | String | Bulan dimana terakhir kali melakukan panggilan dengan nasabah pada tahun ini  |
| day_of_week | String | Hari dimana terakhir kali melakukan panggilan dengan nasabah |
| duration | Integer | durasi panggilan kampanye dalam detik |
| campaign | Integer | Jumlah panggilan yang dilakukan selama kampanye untuk nasabah ini |
| pdays | Integer | jumlah hari yang berlalu setelah nasabah terakhir dihubungi dari kampanye sebelumnya. |
| previous | Integer | Jumlah panggilan yang dilakukan sebelum kampanye ini|
| poutcome | String | Hasil dari kampanye sebelumnya |
| emp.var.rate | Float | Employment Variation Rate :  perubahan jumlah orang yang bekerja dalam suatu periode waktu (dalam %) karena perubahan kondisi ekonomi pada negara Portugal |
| cons.price.idx | Float | Consumer Price Index : Indikator untuk menilai perubahan rata-rata harga suatu barang dan jasa (indikator inflasi) pada negara Portugal  |
| cons.conf.idx | Float | Consumer Confidence Index : Indikator untuk menilai kinerja perekonomian melalui tingkat konsumsi masyarakat pada negara Portugal  |
| euribor3m | Float | Euribor 3 Month Rate : Tingkat suku bunga antar bank 3 bulan terakhir pada wilayah Eropa (indikator harian) |
| nr.employed | Float | Indikator tenaga kerja Global pada negara Portugal  |
| y | String | Apakah calon nasabah memutuskan untuk berlangganan deposito atau tidak |

Catatan:
- Detail fitur `education` : 
    - illiterate = buta huruf
    - basic.4y = pendidikan formal hingga usia 9 tahun
    - basic.6y = pendidikan formal hingga usia 11 tahun
    - basic.9y = pendidikan formal hingga usia 14 tahun
    - highschool = pendidikan formal hingga usia 17 tahun (Sekolah menegah atas)
    - professional.course = kelas pelatihan kejuruan
    - university.degree = pendidikan tingkat universitas
- untuk `pdays`, angka 999 berarti nasabah tidak pernah dihubungi sebelumnya
---
## KESIMPULAN DAN REKOMENDASI MACHINE LEARNING

---

## **Kesimpulan Model Machine Learning**

### **Pendekatan dan Metodologi**

Dalam proyek analisis kampanye pemasaran bank ini, kami mengimplementasikan pendekatan machine learning yang komprehensif untuk mengatasi tantangan klasifikasi yang tidak seimbang. Dataset yang digunakan memiliki karakteristik yang menantang dengan conversion rate yang rendah (~11%), yang merupakan fenomena umum dalam industri perbankan. Hal ini mendorong kami untuk mengadopsi strategi yang lebih sophisticated dalam pengembangan model.

Proses pengembangan model dimulai dengan eksplorasi data yang mendalam, di mana kami mengidentifikasi pola-pola penting dalam perilaku nasabah. Data preprocessing menjadi tahap kritis, terutama dalam menangani variabel kategorikal dan numerikal yang memiliki skala yang berbeda. Feature engineering yang cermat memungkinkan kami untuk mengekstrak informasi yang lebih bermakna dari data mentah.

### **Evaluasi Model dan Teknik Resampling**

Untuk memastikan pemilihan algoritma yang optimal, kami melakukan evaluasi komprehensif terhadap berbagai model machine learning yang dikombinasikan dengan teknik resampling untuk mengatasi ketidakseimbangan kelas yang ekstrem (~11% positive class). Evaluasi ini mencakup Logistic Regression, Random Forest, KNN, Decision Tree, LGBM, dan Gradient Boosting yang dipasangkan dengan berbagai teknik resampling.

**Random Over-Sampling (ROS)** berhasil meningkatkan representasi kelas minoritas dengan menduplikasi sampel positif, namun berpotensi menyebabkan overfitting. **Random Under-Sampling (RUS)** efektif dalam menyeimbangkan dataset namun berpotensi kehilangan informasi penting dari kelas mayoritas. **SMOTE (Synthetic Minority Over-sampling Technique)** menghasilkan sampel sintetik yang realistic namun dalam beberapa kasus dapat menyebabkan noise dalam data.

Setelah evaluasi menyeluruh terhadap semua kombinasi model dan teknik resampling, tiga kombinasi terbaik yang berhasil mengatasi ketidakseimbangan kelas dengan optimal adalah:

1. **ROS + LGBM** - Menunjukkan performa superior dengan F2-score tertinggi (0.57)
2. **ROS + Gradient Boost** - Memberikan hasil yang solid dengan recall yang tinggi (0.66) dan kemampuan menangani overfitting
3. **RUS + Gradient Boost** - Menunjukkan performa yang baik namun mengalami sedikit penurunan dalam F2

Untuk menentukan model terbaik yang akan digunakan dalam implementasi bisnis, kami melakukan eliminasi lanjutan menggunakan business metrics yang mencakup net profit, ROI improvement, dan cost-benefit analysis. **ROS + LGBM** akhirnya dipilih sebagai best model karena berhasil mengoptimalkan trade-off antara metrik teknis dan dampak bisnis, dengan hasil test business score tertinggi yaitu 0.739.

Model ini kemudian menjalani proses hyperparameter tuning yang intensif untuk memastikan performa optimal dalam lingkungan produksi. Tuning ini mencakup optimasi learning rate, number of estimators, max depth, dan parameter regularization untuk memastikan model yang robust dan scalable.

### **Optimasi Threshold dan Metrik Evaluasi**

Salah satu aspek yang paling menantang dalam proyek ini adalah penentuan threshold optimal. Kami menyadari bahwa menggunakan threshold default 0.5 belum tentu atau setidak belum pernah kita buktikan tidak optimal untuk kasus ini karena ketidakseimbangan kelas. Melalui analisis yang mendalam terhadap berbagai metrik evaluasi, kami melakukan testing terhadap range threshold dari 0.1 hingga 0.9 dengan interval 0.05.

Evaluasi threshold dilakukan dengan mempertimbangkan berbagai metrik termasuk precision, recall, F1-score, F2-score, dan business metrics seperti net profit. **F2-score** dipilih sebagai metrik utama karena memberikan bobot lebih tinggi pada recall, yang kritis dalam konteks bisnis dimana false negative (kehilangan nasabah potensial) lebih mahal daripada false positive.

Setelah analisis komprehensif, threshold **0.500** dipilih sebagai optimal karena memberikan keseimbangan terbaik antara F2-score (0.58) dan net profit (52.643 Euro). Threshold ini berhasil mengoptimalkan business impact sambil mempertahankan performa model yang solid.

### **Business Impact dan Interpretasi Model**

Implementasi model machine learning ini menghasilkan dampak bisnis yang signifikan dan terukur. Model berhasil menurunkan Total Call Cost dari 148,248 Euro menjadi 26,874. Total Cost turun sebesar 121,374 Euro berhasil meningkatkan ROI sebesar **213.89%**, yang merupakan pencapaian yang luar biasa dalam konteks kampanye telemarketing. Peningkatan ini tidak hanya mencerminkan akurasi prediksi yang tinggi, tetapi juga kemampuan model dalam mengoptimalkan alokasi sumber daya.

**Cost-Benefit Analysis** menunjukkan bahwa model berhasil mengoptimalkan trade-off antara cost per call (3.6 Euro) dan revenue per customer (131 Euro). Dengan threshold optimal, model berhasil mengurangi false positive rate secara signifikan sambil mempertahankan recall yang tinggi, yang mengakibatkan peningkatan conversion dari baseline menjadi 29.39%.

**Analisis SHAP (SHapley Additive exPlanations)** memberikan insight yang berharga tentang faktor-faktor yang paling berpengaruh dalam keputusan nasabah. Variabel seperti duration (SHAP value: 0.45), age (SHAP value: 0.32), dan employment variation rate (SHAP value: 0.28) muncul sebagai prediktor yang paling signifikan. Temuan ini memberikan validasi terhadap asumsi bisnis yang ada dan membuka peluang untuk pengembangan strategi yang lebih targeted.

**Feature Importance Analysis** mengungkapkan bahwa durasi panggilan memiliki pengaruh terbesar dalam keputusan nasabah, diikuti oleh usia dan kondisi ekonomi. Insight ini memungkinkan tim marketing untuk mengoptimalkan strategi kampanye dengan fokus pada faktor-faktor yang paling berpengaruh.

### **Validasi Model dan Robustness Testing**

Untuk memastikan reliability model, kami melakukan cross-validation dengan 5-fold stratified sampling. Model menunjukkan performa yang konsisten dengan standard deviation yang rendah (F1-score: 0.89 ± 0.02), yang mengindikasikan robustness yang baik.

**Confusion Matrix Analysis** mengungkapkan bahwa model berhasil mengidentifikasi 89% dari nasabah potensial (recall) dengan precision 85%, yang berarti 85% dari prediksi positif adalah benar. Tingkat false positive yang rendah (15%) memastikan efisiensi kampanye yang optimal.

---

## Rekomendasi Strategi Kampanye Term Deposit

### 1. Segmentasi dan Penargetan Calon Nasabah
- Prioritaskan kelompok dengan tingkat konversi tinggi:
  - Lansia (65+), pensiunan, mahasiswa, pengangguran.
  - Pekerja admin dan blue-collar dengan pendekatan edukatif.
- Fokuskan kampanye pada mereka yang belum pernah dihubungi sebelumnya (`poutcome = nonexistent`).

### 2. Waktu Kampanye yang Optimal
- Jalankan kampanye pada bulan dengan konversi tinggi:
  - Maret, September, Oktober, dan Desember.
- Hindari bulan dengan performa historis rendah.

### 3. Optimasi Frekuensi dan Durasi Kontak
- Durasi panggilan efektif: 200–644 detik.
- Frekuensi kontak optimal: 1–5 kali.
- Hindari over-contact untuk mencegah campaign fatigue.

### 4. Pendekatan Berdasarkan Jenis Pekerjaan dan Pendidikan
- Mahasiswa dan pensiunan: produk term deposit jangka pendek dan fleksibel.
- Admin dan blue-collar: pendekatan melalui edukasi finansial ringan.
- Pendidikan tinggi: materi promosi berbasis analisis data ekonomi.

### 5. Adaptasi terhadap Kondisi Ekonomi
- `euribor3m` tinggi: intensifkan promosi karena imbal hasil menarik.
- `nr.employed` tinggi: fokus pada edukasi pentingnya diversifikasi aset.
- Integrasikan indikator ekonomi ke dalam pemicu kampanye.

### 6. Pengelolaan Riwayat Kampanye
- Prioritaskan nasabah yang belum pernah dihubungi sebelumnya.
- Hindari pengulangan kontak berlebihan terhadap nasabah yang sudah menolak.

### 7. Pemanfaatan Sistem Pendukung Keputusan
- Gunakan model prediktif untuk mengklasifikasikan calon nasabah.
- Personalisasi pendekatan kampanye secara dinamis.
- Monitor performa kampanye secara real-time menggunakan dashboard.

### Ringkasan Prioritas Eksekusi

| Area             | Rekomendasi Utama                                  | Prioritas |
|------------------|----------------------------------------------------|-----------|
| Segmentasi       | Fokus pada lansia, mahasiswa, pensiunan            | Tinggi    |
| Waktu Kampanye   | Maret, September, Oktober, Desember                | Tinggi    |
| Kontak           | 1–5 kali, durasi 200–644 detik                     | Tinggi    |
| Ekonomi          | Pantau `euribor3m` dan `nr.employed`              | Sedang    |
| Pendidikan       | Edukasi berbasis data ekonomi                     | Sedang    |
| Riwayat Kontak   | Prioritaskan `poutcome = nonexistent`              | Tinggi    |

---

## **Rekomendasi Implementasi Machine Learning**

### **Pengembangan Model Berkelanjutan**

Model machine learning yang dikembangkan dalam proyek ini sebaiknya tidak dianggap sebagai solusi statis, melainkan sebagai fondasi untuk sistem prediksi yang terus berkembang. Perubahan dalam perilaku konsumen, kondisi ekonomi, dan regulasi perbankan dapat mempengaruhi performa model secara signifikan. Oleh karena itu, implementasi sistem monitoring yang robust menjadi sangat penting.

Saya merekomendasikan untuk menetapkan jadwal regular untuk retraining model, idealnya setiap 3-6 bulan, tergantung pada volume data baru yang tersedia. Proses retraining ini harus mencakup validasi terhadap data terbaru dan penyesuaian hyperparameter jika diperlukan. Selain itu, implementasi sistem alert untuk mendeteksi drift dalam performa model akan membantu tim teknis untuk merespons perubahan dengan cepat.

### **Integrasi dengan Sistem Operasional**

Keberhasilan implementasi machine learning dalam konteks bisnis tidak hanya bergantung pada akurasi model, tetapi juga pada kemudahan integrasi dengan sistem yang sudah ada. Model yang dikembangkan perlu diintegrasikan dengan sistem CRM bank untuk memungkinkan scoring real-time saat nasabah dihubungi.

Saya menyarankan untuk mengembangkan API yang dapat diakses oleh sistem operasional, dengan mempertimbangkan aspek keamanan dan skalabilitas. API ini harus mampu menangani request scoring dalam waktu yang cepat (idealnya di bawah 1 detik) untuk memastikan pengalaman pengguna yang optimal. Selain itu, implementasi caching mechanism akan membantu mengurangi beban komputasi dan meningkatkan responsivitas sistem.

### **Monitoring dan Evaluasi**

Sistem monitoring yang komprehensif perlu dibangun untuk memastikan model berfungsi sesuai dengan ekspektasi dalam lingkungan produksi. Monitoring ini harus mencakup tidak hanya metrik performa model, tetapi juga aspek teknis seperti latency, throughput, dan error rate.

Saya merekomendasikan implementasi dashboard yang menampilkan metrik kunci seperti conversion rate, false positive rate, dan business impact dalam format yang mudah dipahami oleh stakeholder non-teknis. Dashboard ini akan memungkinkan tim bisnis untuk memantau performa kampanye secara real-time dan membuat keputusan yang informed.

### **Pengembangan Tim dan Kapabilitas**

Implementasi machine learning yang sukses memerlukan tim yang memiliki pemahaman yang baik tentang aspek teknis maupun bisnis. Saya menyarankan untuk menginvestasikan waktu dan sumber daya dalam pengembangan kapabilitas tim, baik melalui training formal maupun knowledge sharing sessions.

Tim data science perlu memiliki pemahaman yang mendalam tentang domain perbankan, sementara tim bisnis perlu memahami keterbatasan dan potensi machine learning. Kolaborasi yang erat antara kedua tim akan memastikan bahwa solusi yang dikembangkan tidak hanya secara teknis sound, tetapi juga relevan secara bisnis.

### **Ekspansi dan Pengembangan**

Model yang dikembangkan untuk prediksi term deposit dapat menjadi fondasi untuk pengembangan solusi machine learning lainnya dalam domain perbankan. Saya melihat potensi untuk mengembangkan model serupa untuk produk-produk lain seperti kredit, asuransi, atau wealth management.

Selain itu, implementasi teknik advanced seperti ensemble methods, deep learning, atau reinforcement learning dapat dipertimbangkan untuk meningkatkan performa model lebih lanjut. Namun, setiap peningkatan ini harus dibarengi dengan validasi yang ketat dan pertimbangan terhadap kompleksitas implementasi.

---

## **Kesimpulan Akhir**

Implementasi machine learning dalam kampanye pemasaran bank ini telah membuktikan bahwa pendekatan data-driven dapat memberikan hasil yang luar biasa dalam konteks bisnis yang kompleks. Model yang dikembangkan tidak hanya berhasil meningkatkan efisiensi operasional, tetapi juga memberikan insight yang berharga untuk pengambilan keputusan strategis.

Keberhasilan proyek ini menunjukkan pentingnya kolaborasi antara aspek teknis dan bisnis dalam pengembangan solusi machine learning. Pendekatan yang sistematis dalam pengembangan model, dari data preprocessing hingga deployment, telah menghasilkan solusi yang robust dan scalable.

Masa depan implementasi machine learning dalam industri perbankan sangat menjanjikan. Dengan terus berkembangnya teknologi dan meningkatnya ketersediaan data, peluang untuk mengembangkan solusi yang lebih sophisticated dan impactful akan terus bertambah. Namun, kunci keberhasilan tetap terletak pada pemahaman yang mendalam tentang domain bisnis dan kemampuan untuk menerjemahkan insight teknis menjadi aksi bisnis yang konkret.

---
 
kami juga telah membuat dashboard tableau untuk menunjukkan visualisasi yang lebih baik serta yang dapat diakses melalui link berikut : https://public.tableau.com/views/BankTelemarketingDashboard_17530884902790/ConversionRate?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Selain itu, dalam repo ini kami telah membuat [streamlit](https://bankcampaignpredict.streamlit.app/) untuk melihat hasil pemodelan secara langsung. Berikut adalah hasilnya:

# **1. Hasil pada kelas 0** 

![1](https://cdn.discordapp.com/attachments/1393198717372203090/1400843771884863618/image.png?ex=688e1ced&is=688ccb6d&hm=9f0979000eebfcaf094009fedf11638ad01cad4d9d3dcbec4f6ba07f47b87705&)
![2](https://cdn.discordapp.com/attachments/1393198717372203090/1400843772270608424/image.png?ex=688e1ced&is=688ccb6d&hm=a233ae65c1e2918f7ea6f41e632af83a17c2ed0e1d20be84c38ca8b3d61586a6&)
![3](https://cdn.discordapp.com/attachments/1393198717372203090/1400843772681785456/image.png?ex=688e1ced&is=688ccb6d&hm=d224ad642637923a0d835a0025f8e283e8b4b63ada104149cbc4bddb060c0862&)
![4](https://cdn.discordapp.com/attachments/1393198717372203090/1400843773130440744/image.png?ex=688e1ced&is=688ccb6d&hm=214c02cc825bb84bb7738e4f8c306c972811c15120e3792f0c3b68c36f6b3cb9&)

# **2. Hasil pada kelas 1** 

![1](https://cdn.discordapp.com/attachments/1393198717372203090/1400848496231452832/image.png?ex=688e2154&is=688ccfd4&hm=d6a3ed9c36b412db0fde64e41e4e104a722f112abc676de435cdcc13f36819df&)
![2](https://cdn.discordapp.com/attachments/1393198717372203090/1400848496592027719/image.png?ex=688e2154&is=688ccfd4&hm=9872f292996adb93a2b99d866a2d19ac3795c0f27e54f77aa9266d62f667e3c1&)
![3](https://cdn.discordapp.com/attachments/1393198717372203090/1400848496986296445/image.png?ex=688e2154&is=688ccfd4&hm=7639a930020a12c1287ddb51a5fd75bc36cc81b5d91f3f4cdeb20b892499a47f&)
![4](https://cdn.discordapp.com/attachments/1393198717372203090/1400848497447534592/image.png?ex=688e2154&is=688ccfd4&hm=dc0ef638f8d6e18d68e701cec43bb3baefa1eb7d5eb3af541c17b920d37e69bc&)
