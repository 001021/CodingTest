n, m = map(int, input().split())#s, m 입력
s = list(map(int, input().split()))
s = s[:n]#출제자들이 나눠줄 돈
result =  [0] *(n+m)
for i in range(0, n):
    money = s[i]
    d = list(map(int, input().split()))
    result = [result[i] + d[i] for i in range(len(d))]
    result[i] = result[i]+(money - sum(d))
for data in result:
    print(data, end=" ")
