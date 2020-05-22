s=list(map(str,input()))
#print(s)
for i in range(len(s)):
    if s[i]=='A':
        sa=i
        break

for i in range(len(s)-1,-1,-1):
    if s[i]=='Z':
        zg=i
        break

print(zg-sa+1)