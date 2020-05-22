s=str(input())
count_w=0
ans=0
for i in range(len(s)):
    if s[i:i+1]=='W':
        ans+=i-count_w
        count_w+=1

print(ans)
