# Cara 1
userInput = input().split()
angka1 = float(userInput[0])
angka2 = float(userInput[1])

print(f"{angka2 / angka1 * 100:.4f}%")

# Cara 2
a3, a4 = map(float, input().split())
print(f"{a4 / a3 * 100:.4f}%")
