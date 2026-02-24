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
