s=str(input())
ans=set()
for i in range(len(s)):
    ans.add(s[i])

for i in range(len(s)-1):
    ans.add(s[i:i+2])
    ans.add('.'+s[i+1])
    ans.add(s[i]+'.')
for i in range(len(s)-2):
    ans.add(s[i:i+3])
    ans.add(s[i:i+2]+'.')
    ans.add('.'+s[i+1:i+3])
    ans.add(s[i]+'.'+s[i+2])
    ans.add(s[i]+'..')
    ans.add('..'+s[i+2])
    ans.add('.'+s[i+1]+'.')


print(len(ans)+min(len(s),3))