def sugar(n):
    max = int(n/5)
    for i in range(max, -1, -1):
        tmp = n - i*5
        if(tmp%3 ==0):
            j = tmp/3
            return int(i+j)
    return -1
n = int(input()) 
print(sugar(n))
