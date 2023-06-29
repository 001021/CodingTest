N = int(input())
for i in range(1,N+1):
  num = sum((map(int, str(i))))
  n_sum = num + i
  if(n_sum == N):
    print(i)
    break;
  if(i==N):
    print(0)