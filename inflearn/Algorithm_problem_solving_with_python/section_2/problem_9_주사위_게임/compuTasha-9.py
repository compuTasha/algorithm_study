# 주사위 게임

n = int(input())

max = 0

for i in range(n):
    temp = input().split()
    temp.sort()
    a, b, c = map(int, temp)
    if a == b and b == c:
        ans = 10000 + (a * 1000)
    elif a == b or a == c:
        ans = 1000 + (a * 100)
    elif b == c:
        ans = 1000 + (b * 100)
    else:
        ans =  c * 100
    if ans > max:
        max = ans

print(max)