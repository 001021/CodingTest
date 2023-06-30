n = int(input()) # 색종이의 개수
arr = [[0]*100 for i in range(100)]#도화지
for i in range(0, n):
    x, y = map(int, input().split())
    for i in range(x, x+10):#1로 바꾸면서 채우는 방식
        for j in range(y, y+10):
            arr[j][i]=1
arr = sum(arr, [])#1차원 배열로 바꿈
print(arr.count(1))#1인거 새기
