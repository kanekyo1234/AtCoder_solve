s=str(input())
n=len(s)
ans=""
i=0
while i<n:
    ans+=s[i:i+1]
    now=s[i:i+1]
    j=1
    i+=1

    while s[i:i+1]==now:
        i+=1
        j+=1
    ans+=str(j)

print(ans)