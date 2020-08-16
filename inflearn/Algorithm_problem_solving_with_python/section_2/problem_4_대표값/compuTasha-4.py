# 대표값

n = int(input())
score = list(map(int, input().split()))
avg = sum(score) / n
avg = round(avg)
min = 100000

for i, num in enumerate(score):
    temp = abs(num-avg)
    if temp < min:
        min = temp
        val = num
        idx = i+1
    elif temp == min:
        if num > val:
            val = num
            idx = i+1

print(avg, idx)
