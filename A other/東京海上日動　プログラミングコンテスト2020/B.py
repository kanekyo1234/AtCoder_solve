a,v = map(int,input().split())
b,w = map(int,input().split())
t=int(input())
c=a-b
g=v-w
#print(c,g)
if g<=0:
    if a==b:
        print("YES")
        exit()
    else:
        print("NO")
        exit()
if a<b:
        
    if abs(c)%abs(g)==0 and abs(c)<=g*t:
        print("YES")
    else:
        print("NO")

elif a>b:
    if abs(c)%abs(g)==0 and 
        print("YES")
    else:
        print("NO")

else:
    print("YES")