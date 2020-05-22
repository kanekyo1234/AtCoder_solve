import collections
n,p=map(int,input().split())
factor=[]
if n==1:
    print(p)
    exit()
for i in range(2,int(p**0.5)+1):
    while p%i==0:
        p=p//i
        factor.append(i)
#print(factor)
if not factor:
    print(1)
    exit()
ans=1
a=collections.Counter(factor)

for s,v in a.items():
    ans*=s**(v//n)
print(ans)