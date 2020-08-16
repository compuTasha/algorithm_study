import sys
#sys.stdin = open("input.txt", "rt")

n,k = map(int, input().split())
a = list(map(int,input().split()))
res = set() #공통적인게 없어야하니까

for i in range(n):
        for j in range(i+1,n):
                for m in range(j+1,n):
                        res.add(a[i]+a[j]+a[m])
#원래 내 코드에서는 list로 만들고 공통적인걸 제거하는 방법으로 했는데
#정답코드는 set을 사용함.

res = list(res)
res.sort(reverse=True)
print(res[k-1])
