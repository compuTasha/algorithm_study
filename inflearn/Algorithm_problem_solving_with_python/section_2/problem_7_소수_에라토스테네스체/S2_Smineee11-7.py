import sys
import math
#sys.stdin = open("input.txt", "rt")

n = int(input())


def Prime(n):
        isprime = [True] * (n+1)
        for i in range(2, math.ceil(math.sqrt(n))):
                if isprime[i]:
                           for j in range(2*i,n,i):
                                   isprime[j] = False
        
        return isprime

a = Prime(n)

if(n==2):
        print("1")
else:

        cnt = 0
        for i in range(2,n):
                if a[i] == True:
                        cnt +=1
        print(cnt)
                
