# Sequential Program - Serial Computing
# Menjumlahkan bilangan 1 sampai n secara berurutan

n = 5                 # batas angka
total = 0             # variabel penampung hasil

print("Serial Computation Process")

for i in range(1, n + 1):
    total += i
    print(f"Step {i}: total = {total}")

print("Final Serial Sum =", total)