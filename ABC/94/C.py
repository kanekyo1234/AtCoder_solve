import copy
n=int(input())

x=list(map(int,input().split()))
b=copy.copy(x)
x.sort()
med=(x[n//2-1]+x[n//2])/2
for i in range(n):
    if b[i]<med:
        print(x[n//2])
    else:
        print(x[n//2-1])