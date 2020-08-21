#import sys
#sys.stdin = open("in2.txt", "rt")

N = int(input())
test = list(map(int, input().split()))

cnt=0
result=0
for i in range(N):
    if test[i]==0:
        cnt=0
    elif test[i]==1 and cnt>0:
        cnt+=1
        result+=cnt
    else:
        cnt=1
        result+=cnt
print(result)