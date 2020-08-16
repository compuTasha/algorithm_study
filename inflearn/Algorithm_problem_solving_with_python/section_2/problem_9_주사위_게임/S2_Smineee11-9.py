import sys

#sys.stdin=open("input.txt", "r")

n = int(input())


max = -100000

for i in range(n):
    ary = input().split()
    ary.sort(reverse = False)
    num1 = int(ary[0])
    num2 = int(ary[1])
    num3 = int(ary[2])
    
    if num1==num2 and num1 == num3: #모두 다 같음
        money = 10000+num1*1000
    elif num1 == num2 or num2 == num3 or num1 == num3:
        if num1 == num2 or num1 == num3:
            money = 1000 + num1*100
        else:
            money = 1000 + num2*100
    else: #모두 다 다름
        money = num3*100
    if max<money:
        max = money

print(max)
