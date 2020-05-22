n,k=map(int,input().split())
s=int(n**0.5)
div=2
if k==1:
    if n==1:
        print(-1)
    else:
        print(n)
    exit()
c=0
ans=[]
for i in range(s+1):
    if n%div==0:
        c+=1
        ans.append(div)
        n=n//div
    else:
        div+=1
    if (k-1)==c:
        if n!=1:

            for i in range(c):
                print(ans[i],end=" ")
            print(n)
            exit()
print(-1)





