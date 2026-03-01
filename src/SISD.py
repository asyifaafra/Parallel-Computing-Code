# SISD (Single Instruction Single Data)

n = 5
total = 0

print("SISD Process:")

for i in range(1, n + 1):
    total += i
    print(f"Step {i}: total = {total}")

print("Final SISD Sum =", total)