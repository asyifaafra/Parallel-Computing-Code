from multiprocessing import Process, Queue

# Fungsi untuk menghitung sebagian jumlah
def partial_sum(start, end, q, pid):
    s = sum(range(start, end + 1))
    print(f"Process {pid}: sum({start} to {end}) = {s}")
    q.put(s)

if __name__ == "__main__":
    print("Parallel computation")
    q = Queue()

    # Membagi pekerjaan ke dua proses (simulasi 2 core)
    p1 = Process(target=partial_sum, args=(1, 3, q, 1))
    p2 = Process(target=partial_sum, args=(4, 5, q, 2))

    # Menjalankan proses secara paralel
    p1.start()
    p2.start()

    # Menunggu kedua proses selesai
    p1.join()
    p2.join()

    # Menggabungkan hasil dari masing-masing proses
    total = q.get() + q.get()

    print("Final Parallel Sum =", total)