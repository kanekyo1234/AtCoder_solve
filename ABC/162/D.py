n=int(input())

ans=0
s=list(str(input()))
r=[]
b=[]
g=[]
for i in range(n):
    if s[i]=='R':
        r.append(i)
    if s[i]=='B':
        b.append(i)
    if s[i]=='G':
        g.append(i)
count=0
aida=1

while aida*2-1<=n:
    for i in range(n-aida*2):
        #print("DF")
       # print(s[i],i,s[i+aida],i+aida,s[i+aida*2],i+aida*2)
        aa=set()
        aa.add(s[i])
        aa.add(s[i+aida])
        aa.add(s[i+aida*2])
        #print(aa)
        if len(aa)==3:
            count+=1
    aida+=1
#print(count)

print(len(r)*len(b)*len(g)-count)

"""
for i in range(len(r)):
    for j in range(len(b)):
        for z in range(len(g)):
            mi=min(r[i],b[j],g[z])
            ma=max(r[i],b[j],g[z])
            ad=r[i]+b[j]+g[z]-mi-ma
            if ad-mi!=ma-ad:
               # print(mi,ad,ma)
                ans+=1
print(ans)
#RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBBRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB
"""