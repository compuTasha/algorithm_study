#import sys
#sys.stdin = open("in1.txt", "rt")

def digit_sum(x):
    sum = 0
    while x>=10:
        sum += x%10
        x //= 10
    sum += x
    return sum

N = int(input())
num = list(map(int, input().split()))

max = 0
index = 0
for i in range(N):
    sum = digit_sum(num[i])
    if max<sum:
        max = sum
        index = i
print(num[index])