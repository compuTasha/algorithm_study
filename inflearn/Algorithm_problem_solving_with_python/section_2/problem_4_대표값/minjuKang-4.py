#import sys
#sys.stdin = open("in2.txt", "rt")

N = int(input())
score = list(map(int, input().split()))

avg = round(sum(score)/N, 0)
min = float('inf')
index = 0

for i in range(N):
    dev = abs(score[i]-avg)
    if min>dev:
        min = dev
        index = i
    elif min==dev and score[index]<score[i]:
        index = i

print(int(avg),index+1)
