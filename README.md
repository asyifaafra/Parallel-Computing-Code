## ✍️ Identitas
- Nama: Asyifa Afra Sayyida
- NRP : 15-2024-209
- Mata Kuliah: Komputasi Paralel dan Sistem Terdistribusi - AA

## 💻 Tugas Komputasi Paralel dan Sistem Terdistribusi
Implementasi Parallel Computing Code

## 📌 Deskripsi Proyek
1. Repository ini berisi implementasi sederhana pemrograman komputasi sekuensial (serial computing) dan komputasi paralel (parallel computing) menggunakan bahasa pemrograman Python. Selain itu, repository ini juga menampilkan contoh penerapan empat tipe arsitektur komputasi paralel berdasarkan klasifikasi Flynn, yaitu SISD, SIMD, MISD, dan MIMD.
2. Program dibuat untuk memenuhi tugas mata kuliah Komputasi Paralel dan Sistem Terdistribusi pada Program Studi Informatika. Setiap program dirancang dengan contoh kasus yang sama, yaitu perhitungan penjumlahan angka 1 sampai 5, agar perbedaan cara pemrosesan pada masing-masing arsitektur dapat terlihat dengan jelas.
3. Implementasi yang dibuat meliputi:
- Program SISD yang menjalankan proses secara berurutan (serial).
- Program SIMD yang menggunakan satu instruksi untuk memproses beberapa data sekaligus.
- Program MISD yang menerapkan beberapa instruksi berbeda pada data yang sama.
- Program MIMD yang membagi pekerjaan ke beberapa proses dan dijalankan secara paralel menggunakan multiprocessing.
4. Tujuan dari proyek ini adalah untuk memahami perbedaan cara kerja pemrosesan data secara berurutan dan secara bersamaan menggunakan beberapa inti prosesor, serta melihat bagaimana pembagian instruksi dan data memengaruhi model komputasi yang digunakan.
5. Melalui perbandingan ini, dapat dipahami bahwa meskipun hasil akhir perhitungan tetap sama, mekanisme eksekusi program pada setiap arsitektur memiliki karakteristik dan konsep yang berbeda.
   
## 📂 Struktur Repository
Parallel-Computing-Code/
├── src/
├── docs/
├── output/
├── README.md
└── requirements.txt

## ▶️ Cara Menjalankan Program
1. Program Sequential
python serial_computation.py
2. Program Parallel
python parallel_computation.py
3. Program SISD
python SISD.py
4. Program SIMD
python SIMD.py
5. Program MISD
python MISD.py
6. Program MIMD
python MIMD.py

