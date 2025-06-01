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
🔗 [Dashboard Jaya Jaya Institut](https://lookerstudio.google.com/reporting/b76909a3-8933-4bf7-a35c-4f59afbceb94)

![Dashboard Jaya Jaya Institut](https://raw.githubusercontent.com/satriakipang/Projek-Permasalan-Institusi-Pendidikan/refs/heads/main/fransiskus_ricardo%20-%20dashboard.jpg)

Pada dashboard di digunakan untuk:
* Memahami pola dan faktor yang mempengaruhi **Dropout** siswa.
* Memberikan insight data visual bagi kampus untuk mengambil keputusan strategis terkait siswa yang berpotensi Dropout.

Bagian-Bagian Dashboard
1. **Distribusi Status Mahasiswa**
* Dari total **3.630 data mahasiswa**, sebanyak **60,9%** berhasil lulus (Graduate), dan **39,1%** mengalami dropout.
* Insight: Angka dropout cukup tinggi dan memerlukan perhatian khusus.

2. **Distribusi Gender**
* Mahasiswa laki-laki mendominasi populasi (**65,6%**), sedangkan perempuan **34,4%**.
* Insight: Distribusi ini penting sebagai konteks demografis dan dapat dikaitkan dengan dropout jika dikombinasikan dengan variabel lain.

3. **Admission Grade vs Status**
* Mahasiswa dengan **nilai masuk (admission grade) tinggi** cenderung lebih banyak lulus.
* Terlihat peningkatan kelulusan pada grade **99–100**, sementara dropout lebih banyak pada rentang nilai menengah ke bawah.
* Insight: Nilai masuk bisa menjadi indikator awal risiko akademik.

4. **Scholarship Holder vs Status**
* Mahasiswa **penerima beasiswa** memiliki tingkat kelulusan lebih tinggi.
* Dropout lebih sering terjadi pada mahasiswa **non-penerima beasiswa**.
* Insight: Beasiswa berpotensi menjadi intervensi efektif untuk menurunkan angka dropout.

5. **Mata Kuliah Semester 1 vs Status**
* Dropout banyak terjadi pada mahasiswa yang mengambil mata kuliah tertentu di semester awal (contoh: kode 17 dan 18).
* Insight: Beban dan tingkat kesulitan semester awal perlu dievaluasi karena memengaruhi keberlanjutan studi.

6. **Mata Kuliah Semester 2 vs Status**
* Serupa dengan semester 1, terlihat dominasi dropout pada mata kuliah dengan kode tertentu, terutama **kode 11–13**.
* Insight: Monitoring mata kuliah spesifik bisa menjadi strategi preventif dalam mengurangi dropout.



## Menjalankan Sistem Machine Learning
Prototipe machine learning ini dibangun menggunakan platform Streamlit untuk memudahkan proses deployment. Aplikasi ini memungkinkan pengguna memasukkan sejumlah fitur yang diperlukan, kemudian memberikan hasil prediksi mengenai kemungkinan seorang siswa mengalami dropout.

*Penggunaan Secara Online*

1. Akses aplikasi melalui Streamlit Cloud di tautan berikut:
   [https://projek-permasalan-institusi-pendidikan-dicoding.streamlit.app/](https://projek-permasalan-institusi-pendidikan-dicoding.streamlit.app/)
2. Isi seluruh input fitur yang tersedia pada antarmuka aplikasi.
3. Klik tombol **Prediksi Status** untuk melihat hasil prediksi status dropout siswa.

*Penggunaan Secara Lokal (Offline)*

1. Jalankan aplikasi dengan perintah berikut di terminal:

   ```bash
   streamlit run app.py  
   ```
2. Masukkan nilai-nilai fitur pada form input yang muncul di antarmuka.
3. Tekan tombol **Prediksi Status** untuk memperoleh hasil prediksi.

![Deployment Streamlit](https://raw.githubusercontent.com/satriakipang/Projek-Permasalan-Institusi-Pendidikan/refs/heads/main/fransiskus_ricardo%20-%20deployment.png) 
---



## Conclusion
1. **Sekitar 1.419 mahasiswa tercatat tidak menyelesaikan studi (dropout) di Jaya Jaya Institut.**
2. **Faktor utama yang berkontribusi terhadap dropout adalah: Sedikitnya jumlah mata kuliah yang lulus, terutama di semester 1 dan 2, Nilai akademik yang rendah di kedua semester, Nilai masuk (admission grade) yang rendah, Riwayat pendidikan sebelumnya.**
3. **Tingkat dropout di Jaya Jaya Institut adalah sekitar 39%, yang cukup tinggi dan perlu perhatian.** 
4. **Mayoritas mahasiswa yang dropout adalah belum menikah (single).**
5. **Mahasiswa yang dropout umumnya berada di rentang usia 22–25 tahun.**

### Rekomendasi Action Items 
Berikut adalah **tiga rekomendasi profesional** berdasarkan hasil analisis data dropout di Jaya Jaya Institut:
1. **Pendampingan Adaptasi untuk Mahasiswa Pindahan**
   Mahasiswa pindahan memiliki proporsi dropout yang signifikan. Disarankan agar institusi menyediakan program orientasi dan konseling khusus guna membantu mereka beradaptasi dengan lingkungan akademik dan sistem pembelajaran yang baru.

2. **Program Intervensi Akademik Dini**
   Data menunjukkan bahwa performa akademik di semester pertama berpengaruh besar terhadap potensi dropout. Maka, institusi perlu mengidentifikasi mahasiswa dengan nilai rendah sejak dini dan memberikan bimbingan belajar atau kelas remedial secara proaktif.

3. **Monitoring Berkala terhadap Kinerja Akademik Mahasiswa**
   Melakukan evaluasi berkala terhadap capaian akademik setiap semester, terutama pada mata kuliah inti, untuk mendeteksi penurunan performa dan memberikan intervensi sebelum risiko dropout meningkat.
