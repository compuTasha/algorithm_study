import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int,input().split()))


avg = sum(a)/n
roundavg = round(avg)
min = 100000
index = 0
for i in range(0,n):
        tmp= abs(a[i]-roundavg)
        if(min>=tmp):
                if(min>tmp):
                        index=i
                        min = tmp
                if(min==tmp):
                        #print(a[index])
                        if(a[index]<a[i]):
                                index=i
                                min = tmp
print(roundavg,index+1)
