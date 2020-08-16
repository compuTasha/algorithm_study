#import sys
#sys.stdin = open("in2.txt", "rt")

N = int(input())
num = [True]*(N+1)
num[0:2] = [False, False]

for i in range(2, int(N**0.5)+1):
    if num[i]==True:
        for j in range(i*i, N+1,i):
            num[j]= False

print(sum(num))