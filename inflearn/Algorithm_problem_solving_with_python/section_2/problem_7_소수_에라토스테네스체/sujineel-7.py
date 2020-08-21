import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
prime=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if prime[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            prime[j]=1
print(cnt)