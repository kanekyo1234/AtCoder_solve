import math
oa,ab,bc=map(int,input().split())
a=[oa,ab,bc]
maxa=(oa+ab+bc)**2*math.pi
if max(a)>=(sum(a)-max(a)):
    space=(max(a)-(sum(a)-max(a)))**2*math.pi
else:
    space=0
#print(space)
print(maxa-space)