import sys
sys.stdin=open("input.txt", "r")
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

n=int(input())
a=list(map(int, input().split()))
result=0
max=-2147000000
for x in a:
    total=digit_sum(x)
    if total>max:
        max=total
        result=x
print(result)