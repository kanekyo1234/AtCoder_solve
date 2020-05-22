a,b,c=map(int,input().split())
d=[b-c-1]*a
for i in range(c):
    g=int(input())
    d[g-1]+=1
for i in range(len(d)):
    if d[i]>=0:
        print("Yes")
    else:
        print("No")
