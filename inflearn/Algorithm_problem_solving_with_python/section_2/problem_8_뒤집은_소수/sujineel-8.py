import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
def reverse(x):
    result=0
    while x>0:
        y=x%10
        ressult=result*10+y
        x=x//10
    return result

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')


