n=int(input())
a=list(map(int,input().split()))
count=1
x=max(a)
import collections
c=collections.Counter(a)
if a[0]!=0 or c[0]!=1:
  print(0)
  exit()
else:
  b=[1]*(x+1)
  for i in range(1,x+1):
    count=(count*(b[i-1]**c[i]))%998244353
    b[i]=c[i]
  print(count)
