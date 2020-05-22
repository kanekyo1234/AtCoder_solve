
n=int(input())
s=[]
t=[]
for i in range(n):
    a,b=map(str,input().split())

    s.append(a)
    t.append(int(b))

x=str(input())
count=0
for i in range(n):
    if s[i]==x:
        count=i
        break
ans=0
count+=1

for i in range(count,n):
    ans+=t[i]
print(ans)