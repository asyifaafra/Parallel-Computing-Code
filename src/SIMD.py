# SIMD (Single Instruction Multiple Data)
import numpy as np

data = np.array([1, 2, 3, 4, 5])

print("SIMD Process:")

# Satu instruksi untuk semua data
result = data

total = np.sum(result)

print("Data:", data)
print("Final SIMD Sum =", total)