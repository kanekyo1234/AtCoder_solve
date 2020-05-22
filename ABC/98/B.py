n=int(input())
s=str(input())
ans=0
for i in range(n-1):
    a=set(s[i+1:])
    b=set(s[:i+1])
    ans=max(ans,len((a&b)))
print(ans)