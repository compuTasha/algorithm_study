# K번쨰 수

t = int(input())

result = []
cnt = 1

for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()
    print("#%d %d" %(i+1, arr[k-1]))

