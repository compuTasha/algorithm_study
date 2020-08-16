import sys
sys.stdin = open("input.txt", "rt")

n,m = map(int ,input().split())
cnt = [0]*(n*m)

max = -20000

for i in range(1,n+1):
        for j in range(1,m+1):
                sum = i+j
                cnt[sum] +=1
                
for i in range(n+m):
        if cnt[i+1]>max:
                max = cnt[i]

for i in range(n+m+1):
        if cnt[i] ==  max:
                print(i,end=' ')

#왜 n+m일까...?
