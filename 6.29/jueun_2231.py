N = int(input())

min = 10000000

for M in range(N):
    m = M
    sum = 0
    sum += m
    while m > 0:
        sum += (m % 10)
        m = m // 10
    if (sum == N):
        if (min > M):
            min = M

if (min >= 10000000):
    print(0)
else:
    print(min)

