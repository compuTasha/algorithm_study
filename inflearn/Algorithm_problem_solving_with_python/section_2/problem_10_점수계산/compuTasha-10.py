 # 점수계산 (미완성)

n = int(input())
num = list(map(int, input().split()))
score = [0] * (n+1)

for i in range(n):
    if i == 0:
        score[i] = 1
    elif num[i] == 1:
        if num[i] == num[i-1]:
            score[i] == num[i-1] + 1
        else:
            score[i] = 1
    else: continue

print(sum(score))