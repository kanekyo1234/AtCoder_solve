x=list(input())
s=0
t=0
ans=0
for i in range(len(x)):
    if x[i]=="S":
        s+=1

    else:
        if s==0:
            ans+=1
        else:
            s-=1

print(ans+s)