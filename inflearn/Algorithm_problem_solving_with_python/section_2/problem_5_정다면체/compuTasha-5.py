# 정다면체

n, m = map(int, input().split())
sum = [0] * (n+m+1)
max = 0

for i in range(1, n+1):
    for j in range (1, m+1):
        sum[i+j] += 1
for i in range(n+m+1):
    if sum[i] > max:
        max = sum[i]
for i in range(n+m+1):
    if sum[i] == max:
        print(i, end=' ')


