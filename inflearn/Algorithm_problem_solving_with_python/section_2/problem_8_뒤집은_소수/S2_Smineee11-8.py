import sys
import math
#sys.stdin = open("input.txt", "rt")


n = int(input())
a=list(map(int,input().split()))

def isPrime(x):
        getprime = [] 
        isprime = [True] * (x+1)
        for i in range(2, math.ceil(math.sqrt(x))):
                if isprime[i]:
                           for j in range(2*i,x,i):
                                   isprime[j] = False

        for i in range(2,x):
                if isprime[i] == True:
                        getprime.append(i)
        
        return getprime

def reverse(x):
        fulary = []
        for i in x:
                reverseary = []
                tmp = str(i)
                cnt = 0
                totalnum=0
                for j in range(len(tmp)):
                        num = i%10
                        i = int(i/10)
                        reverseary.append(num)
                   
                        cnt +=1
                for k in range(cnt):
                        totalnum += (10 ** (cnt-k-1)) * reverseary[k]

                fulary.append(totalnum)

        return fulary

flag = False
res = reverse(a)
for i in res:
        pri = isPrime(i+1)
       # print(pri)
        for k in pri:
             if i == k:
                     flag = True
        if(flag == True):
                flag = False
                print(i, end = ' ' )
        




