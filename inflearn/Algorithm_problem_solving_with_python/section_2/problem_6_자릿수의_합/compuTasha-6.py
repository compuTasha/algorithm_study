# 자릿수의 합

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x%10
        x = x//10
    return sum

n = int(input())
num = list(map(int, input().split()))
ans = 0
max = -1000000000
for i in num:
    sum = digit_sum(i)
    if sum > max:
        max = sum
        ans = i

print(ans)