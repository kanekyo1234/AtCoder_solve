s=list(str(input()))
n=len(s)
ans=0
for i in range(n):
    if s[i]=='U':
        ans+=n-1+i
    else:
        ans+=n-1+n-1-i
    #print(ans)
print(ans)

         