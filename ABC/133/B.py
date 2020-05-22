import math
a,b=map(int,input().split())
c=[[int(i) for i in input().split()] for i in range(a)]


count=0
sum1=0
sum1=0
for i in range(a):
    for z in range(i+1,a,1):
        for j in range(b):
            sum1+=(c[i][j]-c[z][j])**2
        
        if math.sqrt(sum1)%1.0==0:
            count+=1
        sum1=0
print (count)