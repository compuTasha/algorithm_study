#import sys
#sys.stdin = open("in1.txt", "rt")

def calculate(x):
    money=0
    if x[0]==x[1] and x[1]==x[2]:
        return 10000+x[0]*1000
    elif x[0]==x[1] or x[0]==x[2]:
        return 1000+x[0]*100
    elif x[1]==x[2]:
        return 1000+x[1]*100
    else:
        money = max(x)*100
        return money

N = int(input())
max_num = 0

for i in range(N):
    num = list(map(int, input().split()))
    money = calculate(num)
    if max_num<money:
        max_num = money

print(max_num)
