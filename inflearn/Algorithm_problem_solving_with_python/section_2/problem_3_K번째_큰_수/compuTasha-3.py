# K번째 큰 수

n, k = map(int, input().split())
num = list(map(int, input().split()))
sum = set()

for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
                sum.add(num[i]+num[j]+num[l])

sum = list(sum)
sum.sort(reverse=True)
print(sum[k-1])