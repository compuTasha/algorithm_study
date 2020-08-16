#import sys
#sys.stdin = open("in1.txt", "rt")

N, K = map(int, input().split())
array = list(map(int, input().split()))

sum = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum.add(array[i]+array[j]+array[k])

sum = list(sum)
sum.sort(reverse=True)
print(sum[K-1])
    