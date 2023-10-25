T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    print(f"Case #{t + 1}:")
    for j in range(N):
        for k in range(M):
            if j == 0 or j == N - 1:
                print("#", end=" ")
            elif k == 0 or k == M - 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()
