import math
a,b,c=map(int,input().split())
c=c**0.5
a=a**0.5
b=b**0.5
c-=a
c-=b
if 0<c:
    print("Yes")
else:
    print("No")
    