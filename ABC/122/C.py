n,q=map(int,input().split())
s=str(input())
l=[]
r=[]
for i in range(q):
    a,b=map(int,input().split())
    l.append(a)#文字列の最初
    r.append(b)#文字列の最後

ans=[]
ans.append(0)
count=0
for i in range(n-1):
    if s[i:i+2]=="AC":
        count+=1
        ans.append(count)
    else:
        ans.append(count)

for i in range(q):
    print(ans[r[i]-1]-ans[l[i]-1])


#print(s[2:7])=ACTAC