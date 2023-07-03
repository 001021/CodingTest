N = int(input())

sum = 0

while N >= 0:
  if (N % 5 == 0):
    sum += N // 5
    print(sum)
    break

  N -= 3
  sum += 1

  if N < 0:
    print(-1)
    break
