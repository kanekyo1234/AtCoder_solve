s=str(input())
#print(s)
s=s.split(' ')
a=[]

b=[]
for i in range(len(s)):
    if s[i].count('@')!=0:
        if s[i][0:1]=='@':
            a.append(s[i].split('@'))
        else:
            b.append(s[i].split('@'))
#print(a)

#print(s)
ans=set()
for i in range(len(a)):
    for j in range(len(a[i])):

        if a[i][j]!='':
            ans.add(a[i][j])    

for i in range(len(b)):
    for j in range(1,len(b[i])):

        if b[i][j]!='':
            ans.add(b[i][j])   

ans=sorted(list(ans))
for i in range(len(ans)):
    print(ans[i])