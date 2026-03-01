## 📘 Penjelasan Proses Program Serial Computing
Program di atas merupakan contoh implementasi komputasi sekuensial (serial computing), di mana proses perhitungan dilakukan secara berurutan dalam satu alur eksekusi.
1. Variabel n digunakan sebagai batas bilangan yang akan dijumlahkan.
2. Variabel total berfungsi sebagai penampung hasil penjumlahan sementara.
3. Perulangan for digunakan untuk menambahkan nilai i ke dalam total secara satu per satu.
4. Pada setiap iterasi, program menampilkan hasil akumulasi sementara.
5. Setelah seluruh proses selesai, hasil akhir ditampilkan sebagai jumlah total.

## 📘 Penjelasan Proses Program Parallel Computing 
1. Program menggunakan modul multiprocessing untuk menjalankan beberapa proses secara bersamaan.
2. Fungsi partial_sum() bertugas menghitung jumlah bilangan pada rentang tertentu (misalnya 1–3 dan 4–5).
3. Setiap proses menghitung bagiannya masing-masing tanpa menunggu proses lain.
4. Hasil perhitungan dari setiap proses disimpan ke dalam Queue.
5. Proses start() menjalankan perhitungan secara paralel pada beberapa core.
6. Proses join() memastikan semua proses selesai sebelum hasil digabungkan.
7. Nilai dari Queue dijumlahkan untuk memperoleh hasil akhir.

## 📘 Penjelasan Proses Program SISD (Single Instruction Single Data)
1. Menggunakan satu instruksi untuk memproses satu data dalam satu waktu.
2. Proses penjumlahan dilakukan secara berurutan dari angka 1 sampai 5.
3. Menggunakan satu alur eksekusi (tidak paralel).
4. Sama seperti konsep program serial.

## 📘 Penjelasan Proses Program SIMD (Single Instruction Multiple Data)
1. Menggunakan satu jenis instruksi yang sama untuk banyak data sekaligus.
2. Data disimpan dalam bentuk array.
3. Operasi dilakukan dalam satu perintah untuk seluruh data.
4. Lebih efisien untuk pengolahan data dalam jumlah besar.

## 📘 Penjelasan Proses Program MISD (Multiple Instruction Single Data)
1. Menggunakan beberapa instruksi berbeda pada satu data yang sama.
2. Satu nilai diproses dengan metode perhitungan yang berbeda.
3. Hasil akhir tetap sama meskipun cara perhitungannya berbeda.
4. Jarang digunakan dalam sistem umum, lebih banyak bersifat teoritis.

## 📘 Penjelasan Proses Program MIMD (Multiple Instruction Multiple Data)
1. Menggunakan beberapa instruksi untuk memproses beberapa data secara bersamaan.
2. Data dibagi menjadi beberapa bagian.
3. Proses dijalankan paralel menggunakan multiprocessing.
4. Hasil dari setiap proses digabungkan di akhir.
