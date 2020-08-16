# K번쨰 약수

n, k = map(int, input().split())
d = [1]

for i in range(2, n):
    if n%i == 0:
        d.append(i)
d.append(n)

print(d[k-1])