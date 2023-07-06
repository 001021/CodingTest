N = int(input())

sortList = [0] * 100000
indexList = []
solveList = []

result = ''

for n in range(N):
    inputList = input().split()
    str = inputList[0]
    sortList[int(inputList[1]) - 1] = str[int(inputList[2]) - 1]

for data in sortList:
    if data:
        print(data.upper(), end='')
