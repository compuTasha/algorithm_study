T = int(input())

for t in range(T):
    N, s, e, k = map(int, input().split())
    array = list(map(int, input().split()))
    array = array[s-1:e]
    array.sort()
    print("#%d %d" %(t+1, array[k-1]))

    