import sys
import math
import time
start = time.time()

a = []
sorta = []

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())



for i in range(1, int(math.sqrt(n)+1)):
        if (n%i == 0):
                a.append(int(i))
                if(n/i != i):
                        a.append(int(n/i))
                 
a.sort(reverse=False)


cnt=0



for i in range(0, len(a)+1):
        if(len(a)<k):
                print("-1")
                break
        cnt = cnt +1
        if(cnt == k-1):
                print(a[cnt])
                break
        
print("time: ", time.time() -start)
