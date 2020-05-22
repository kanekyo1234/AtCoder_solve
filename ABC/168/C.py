import math
a,b,h,m=map(int,input().split())

ti=h*30+m*0.5
oo=m*6

#print(ti,oo)

kakudo = abs(ti-oo)-max(0,(abs(ti-oo)-180)*2)
#print(kakudo)

#print(math.cos(kakudo))

c=a**2+b**2 - 2*a*b*math.cos(math.radians(kakudo))
print(c**0.5)