# 뒤집은 소수

def reverse(x):
    ans = 0
    while x > 0:
        temp = x % 10
        ans = ans * 10 + temp
        x = x // 10
    return ans

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
num = list(map(int, input().split()))

for i in num:
    temp = reverse(i)
    if isPrime(temp):
        print(temp, end=' ')

