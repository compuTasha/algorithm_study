#K번째 약수
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

#K번째 수
#import sys
##sys.stdin=open("input.txt", "rt")
#T=int(input())
#for t in range(T):
#	N, s, e, k=map(int, input().split())
#	a=list(map(int, input().split()))
#	a=a[s-1:e]
#	a.sort()
#	print("#%d %d"  %(t+1, a[k-1]))

#K번째 큰 수
import sys
#sys.stdin=open("input.txt", "rt")
n, K= map(int, input().split())
a= list(map(int, input().split()))
#중복을 제거하는 자료구조 : set
res = set()
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			res.add(a[i]+a[j]+a[k])
#set은 sort 기능이 없음
res = list(res)
res.sort(reverse = True)#내림차순 정렬

print(res[K-1])


