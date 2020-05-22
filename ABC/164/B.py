a,b,c,d=map(int,input().split())

acount=0
ccount=0

while 0<a:
    acount+=1
    a-=d


while 0<c:
    ccount+=1
    c-=b

#print(acount,ccount)

if acount<ccount:
    print("No")
else:
    print("Yes")