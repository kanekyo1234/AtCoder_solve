import math
n=int(input())
a=math.sqrt(n)
b=round(a)
for i in range(b,0,-1):
    if n%i==0:
        print(n//i+i-2)
        break

