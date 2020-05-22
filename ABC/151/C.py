"""
a,b=map(int,input().split())
s=[list(map(str,input().split())) for i in range(b)] 
for i in range(b):
    s[i][0]=int(s[i][0])

aans=0
wans=0
c1=0
count=0
dame=[]
for i in range(b-1,-1,-1):
    if s[i][1]=="AC":
        count=i
        break

for i in range(count+1):
    if s[i][1]=="AC":
        if s[i][0] in dame:
            c1+=1
        else:
            dame.append(s[i][0])
            aans+=1
    else:
        wans+=1
print(aans,wans)
"""

a,b=map(int,input().split())

c=[]
for i in range(b):
    d,e=map(str,input().split())
    c.append([int(d),e])

acans=0
waans=0
ac=[0]*(a+1)
wa=[0]*(a+1)
for i in range(b):
    if c[i][1]=="AC":
        if ac[c[i][0]-1]==0:
            acans+=1
            ac[c[i][0]-1]+=1
            waans+=wa[c[i][0]-1]
    else:
        wa[c[i][0]-1]+=1
#print(ac)
#print(wa)
print(acans,waans)