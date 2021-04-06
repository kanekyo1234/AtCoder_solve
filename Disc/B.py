a=int(input())
b=list(map(int,input().split()))
money=0
kei=0
cnt1=0
cnt2=0
if a%2==1:
    for i in range(0,a,1):
        kei+=b[i]
    f=0
    while cnt1<=kei/2:
        cnt1+=b[f]
        f+=1
    cnt1-=b[f-1]
    g=a-1
    while cnt2<=kei/2:
        cnt2+=b[g]
        g-=1
    cnt2-=b[g+1]
else:
    for i in range(0,a,1):
        kei+=b[i]
    f=0
    while cnt1<=kei/2:
        cnt1+=b[f]
        f+=1
    cnt1-=b[f-1]
    g=a-1
    while cnt2<=kei/2:
        cnt2+=b[g]
        g-=1
    cnt2-=b[g+1]
if cnt1==kei/2:
    print(0)
else:
    print(abs(b[f-1]-abs(cnt1-cnt2)))
