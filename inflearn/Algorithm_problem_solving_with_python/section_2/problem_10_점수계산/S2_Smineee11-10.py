import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))

seq = 0
score = 0

for i in range(n):
        if(a[i] == 1):
                seq +=1
                score += score
        else:
                seq = 0

print(score)
