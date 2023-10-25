# Cara cepet
a, b, c = map(float, input().split())

a1 = a * 0.20
b1 = b * 0.30
c1 = c * 0.50

print(f"{a1+b1+c1:.2f}")

# Cara Lama
userInput = input().split()

a = float(userInput[0]) * 0.20
b = float(userInput[1]) * 0.30
c = float(userInput[2]) * 0.50

print(f"{a + b + c:.2f}")
