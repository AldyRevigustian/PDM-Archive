T = int(input())

for t in range(T):
    k, n, m = map(int, input().split())

    if n + m >= k:
        print(f"Case #{t+1}: yes")
    else:
        print(f"Case #{t+1}: no")
