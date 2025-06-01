# Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan
Nama : Fransiskus Ricardo


## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Dalam perjalanannya, institut ini telah menghasilkan banyak lulusan berkualitas dan membangun reputasi yang sangat baik di dunia pendidikan. Namun, tantangan besar tengah dihadapi oleh institusi ini, yaitu angka dropout siswa yang tinggi. Banyak siswa yang tidak menyelesaikan masa studi mereka dan keluar di tengah jalan.

Fenomena dropout ini tidak hanya berdampak pada reputasi akademik institut, namun juga membawa konsekuensi serius dalam hal:
- Efektivitas sistem pendidikan internal,
- Perencanaan sumber daya pengajaran,
- Dan paling penting, keberhasilan akademik para siswa.

Agar kualitas layanan pendidikan tetap terjaga, pihak manajemen ingin dapat mendeteksi lebih awal siswa yang berisiko tinggi mengalami dropout sehingga mereka bisa diberikan intervensi dan bimbingan lebih lanjut.

### Permasalahan Bisnis
Berdasarkan informasi ditas dirumuskan permasalahannya sebagai berikut :
1. **Berapa total jumlah mahasiswa yang tidak menyelesaikan studi (dropout) di Jaya Jaya Institut?**
2. **Faktor-faktor apa saja yang berkontribusi terhadap kemungkinan mahasiswa mengalami dropout?**
3. **Berapakah tingkat dropout (dropout rate) secara keseluruhan di Jaya Jaya Institut?**
4. **Bagaimana distribusi status pernikahan (marital status) dari mahasiswa yang mengalami dropout?**
5. **Berapakah rata-rata usia mahasiswa yang teridentifikasi mengalami dropout?**

### **Cakupan Proyek**
Proyek ini dirancang dengan cakupan:
1. **Eksplorasi dan Pemahaman Awal Data '[students_performance.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)`**
2. **Persiapan dan Pembersihan Data**
3. **Analisis Penyebab Dropout**
4. **Pengembangan Dashboard**
5. **Penarikan Insight dan Rekomendasi Strategis**

### Persiapan
**Sumber data:** [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

**Setup environment:**
- Setup Environment - Anaconda
```
conda create --name projek-institusi-pendidikan python=3.11.7
conda activate projek-institusi-pendidikan
pip install -r requirements.txt
```
- Setup Environment - Shell/Terminal: 
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
atau secara manual:
```
pip install imbalanced_learn imblearn matplotlib numpy pandas scikit_learn seaborn SQLAlchemy
```
- Jalankan seluruh sel dalam file `notebook.ipynb`.

## Business Dashboard
Dashboard dapat diakses dengan link berikut:
🔗 [Dashboard HR](https://lookerstudio.google.com/reporting/6bb4df10-969c-4c7c-883a-bbfbb397e7fe)

![Dashboard HR](https://github.com/satriakipang/Submission-Pertama-Menyelesaikan-Permasalan-HR/blob/main/fransiskus_ricardo%20-%20dashboard.jpg?raw=true)

Pada dashboard di digunakan untuk:
* Memahami pola dan faktor yang mempengaruhi **attrition (resign)** karyawan.
* Memberikan insight data visual bagi manajemen untuk mengambil keputusan strategis terkait retensi.

Bagian-Bagian Dashboard
1. **Age vs Attrition**
* Mayoritas resign terjadi di usia muda (sekitar 26–35 tahun).
* Seiring bertambahnya usia, jumlah resign menurun drastis.

2. **Environment Satisfaction vs Attrition**
* Tingkat kepuasan lingkungan kerja yang rendah (tingkat 1 dan 2) memiliki jumlah resign lebih tinggi.
* Semakin tinggi kepuasan, semakin rendah tingkat resign.

3. **Total Working Years vs Attrition**
* Karyawan dengan pengalaman kerja 0–10 tahun lebih banyak resign.
* Terlihat lonjakan resign di tahun ke-1 dan ke-5, mungkin karena kontrak atau masa evaluasi.

4. **Distance From Home vs Attrition**
* Resign lebih banyak terjadi pada karyawan yang tinggal dekat kantor (jarak 1–5).
* Kemungkinan karena tenaga muda atau first jobber yang lebih rentan pindah kerja.

5. **Persentase Resign (Pie Chart)**
* **16,9%** karyawan resign.
* **83,1%** tetap bekerja.
* Ini menunjukkan tingkat turnover yang moderat tapi perlu perhatian.

6. **Monthly Income vs Age vs Attrition**
* Distribusi gaji berdasarkan usia menunjukkan bahwa resign lebih dominan pada usia muda dengan gaji lebih rendah.
* Ini mengindikasikan perlunya strategi retensi pada kelompok ini.

7. **Model ML**
Pada dashboard diberikan Tabel prediksi model ML yang dapat membantu team HR
* Masing-masing baris berisi atribut karyawan dan kolom:
  * `Attrition (Actual)` = 1 berarti benar-benar resign.
  * `Predicted Attrition` = 1 jika model memprediksi akan resign.
  * `Risk (Probability)` = tingkat risiko (0–1), contoh: 0.99 = 99% kemungkinan resign.



## Conclusion
1. **Gaji rendah, jarak rumah jauh, dan pengalaman kerja sedikit adalah kombinasi utama yang mendorong karyawan keluar.**
2. **Usia muda dan status lajang merupakan segmen yang lebih rentan untuk resign.**
3. **Lembur dan rendahnya sangat berkorelasi dengan attrition.** 
4. **Perlu perhatian khusus terhadap departemen Sales, karena tingka attrition yang tinggi.**
5. **Pegawai yang mengalami attrition (Mengundurkan diri) rerata bekerja selama 8 tahun.**

### Rekomendasi Action Items (Optional)
* **Revisi kompensasi**, khususnya untuk karyawan muda dan berpenghasilan rendah.
* **Program retensi dan engagement** untuk karyawan lajang dan baru.
* **Fleksibilitas kerja atau subsidi transportasi** untuk karyawan yang tinggal jauh dari kantor.
* **Kurangi lembur** dan **tingkatkan kepuasan kerja** melalui survei dan perbaikan lingkungan kerja.
* Fokus pengembangan SDM di departemen dan peran dengan tingkat attrition tinggi.