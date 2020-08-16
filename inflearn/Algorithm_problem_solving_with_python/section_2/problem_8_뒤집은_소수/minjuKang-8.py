#import sys
#sys.stdin = open("in2.txt", "rt")

def reverse(x):
    digit=1
    while x>=digit*10:
        digit *= 10
    result = 0
    while digit>1:
        result += (x%10)*digit
        x //= 10
        digit /= 10
    result += x     
    return result

def isPrime(x):
    if x==1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    else: return True

N = int(input())
num = list(map(int, input().split()))
revList = list(map(reverse, num))

for i in revList:
    if isPrime(i):
        print(int(i), end=' ')
