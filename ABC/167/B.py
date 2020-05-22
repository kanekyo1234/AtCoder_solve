a,b,c,k=map(int,input().split())

ans=0
if a<k:
    ans+=a
    k-=a
else:
    ans+=k
    print(ans)
    exit()

k-=b

#print(k)

if k<0:
    print(ans)
else:
    print(ans-k)