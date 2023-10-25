def is_breakable(s):
    # Menggunakan set untuk menghitung jumlah karakter berbeda
    # karena set tidak bisa memasukan char yang duplicate
    unique_chars = set(s)
    print(unique_chars)
    if len(unique_chars) % 2 == 1:
        return "Unbreakable"
    else:
        return "Breakable"


# Input jumlah test case
T = int(input())

# Loop melalui setiap test case
for i in range(1, T + 1):
    S = input()
    result = is_breakable(S)
    # Menampilkan output sesuai format yang diminta
    print(f"Case #{i}: {result}")
