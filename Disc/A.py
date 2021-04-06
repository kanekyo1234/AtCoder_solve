a,b=map(int,input().split())
count=0

if a==1:
    count+=300000
if a==2:
    count+=200000
if a==3:
    count+=100000
if b==1:
    count+=300000
if b==2:
    count+=200000
if b==3:
    count+=100000
if a==1 and b==1:
    count+=400000

print (count)