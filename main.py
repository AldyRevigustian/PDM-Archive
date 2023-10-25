arrA = ["Aldy", "Revi", "Gustian"]

for x in arrA:
    print("".join(reversed(x)))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Faktorial dari 5 adalah", factorial(5))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
number = 2

while count < 10:
    if is_prime(number):
        count += 1
        print(f"Bilangan prima ke-{count}: {number}")
    number += 1
