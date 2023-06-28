N, M = map(int, input().split())

S_list = list(map(int, input().split()))

T_list = []

for n in range(N):
    T_list.append(list(map(int, input().split())))

result = []

for n in range(N):
    result.append(S_list[n])

for m in range(N + 1, N + M + 1):
    result.append(0)

for i in range(N):
    for j in range(N + M):
        result[i] -= T_list[i][j]
        result[j] += T_list[i][j]

for data in result:
    print(data, end=" ")