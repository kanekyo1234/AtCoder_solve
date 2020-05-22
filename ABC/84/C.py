n=int(input())
c=[]
s=[]
f=[]
for i in range(n-1):
    a,b,d=map(int,input().split())
    c.append(a)
    s.append(b)
    f.append(d)

for i in range(n-1):
    count=0
    for j in range(i,n-1):
        if count<=s[j]:
            count=s[j]
        else:
            if (count-s[j])%f[j]!=0:
                count+=f[j]-((count-s[j])%f[j])
        count+=c[j]
    print(count)

print(0)

