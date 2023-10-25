T = int(input())

for t in range(T):
    S = input()

    result = []

    for i in range(len(S)):
        if 'a' <= S[i] <= 'z':
            result.append(S[i])

    result_str = ''.join(result)

    print(f"Case #{t + 1}: {result_str}")
