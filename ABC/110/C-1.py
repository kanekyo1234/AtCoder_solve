import collections 

s=input()
t=input()
s= collections.Counter(s)
t= collections.Counter(t)
#print(s)
sans=[]
tans=[]

for v in s.values():
    sans.append(v)
for v in t.values():
    tans.append(v)
sans.sort()
tans.sort()
#print(sans,tans)
if sans==tans:
    print('Yes')
else:
    print('No')
