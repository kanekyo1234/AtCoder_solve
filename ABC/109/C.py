import math 
n,m=map(int,input().split())
x=list(map(int,input().split()))

a=[]

x.append(m)
x.sort()
for i in range(n):
    a.append(x[i+1]-x[i])
count=a[0]

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

for i in range(1,len(a)):
    count=gcd(count,a[i])
print(count)