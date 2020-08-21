#import sys
#sys.stdin = open("in2.txt", "rt")

N, M = map(int, input().split())
min = min(N,M)+1
max = max(N,M)+1

for i in range(min, max+1):
    print(i, end=' ')
print()

'''
1,2,3,4 / 1,2,3,4,5,6
2~7
3~8
4~9
5~10
5,6,7

2~5
3~6
4~7
5~8
6~9
7~10
5,6,7

1,2,3,4 / 1,2,3,4
2~5
3~6
4~7
5~8
5
'''