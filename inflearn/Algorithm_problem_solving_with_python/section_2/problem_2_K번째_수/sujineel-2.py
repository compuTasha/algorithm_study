#import sys
#sys.stdin=open("input.txt", "rt")
#n, k=map(int, input().split())
#list=[]
#for i in range(1, n+1):
#	if n%i == 0:
#		list.append(i)
	
#if len(list)>=k:
#	print(list[k-1])
#else:
#	print(-1)

import sys
#sys.stdin=open("input.txt", "rt")
T=int(input())
for t in range(T):
	N, s, e, k=map(int, input().split())
	a=list(map(int, input().split()))
	a=a[s-1:e]
	a.sort()
	print("#%d %d"  %(t+1, a[k-1]))