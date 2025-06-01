# Submission Pertama: Menyelesaikan Permasalahan Institusi Pendidikan
Nama : Fransiskus Ricardo
[Rekaman](https://drive.google.com/file/d/1oT9eWwlTCMR7Wl4Vk-RDwoNjDuSObYQ_/view?usp=sharing)

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

