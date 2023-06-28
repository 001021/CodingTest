def blackjack():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    c.sort()#오름차순
    i=n
    max =0
    while i-3>=0:
        for j in range(i-2, 0, -1):
            for k in range(j-1, -1, -1):
                result = c[i-1]+c[j]+c[k]
                if(result<=m and max<result): 
                    max = result
        i-=1
    return max
print(blackjack())
