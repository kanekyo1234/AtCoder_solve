import copy
n=int(input())
a=list(map(int,input().split()))
b=[i for i in range(2**n)]#indexを入れる
#print(b)
nn=2**n
ans=[0]*(2**n)
match=1
c=[]
while nn!=1:
    for i in range(0,nn,2):
        if a[b[i]]<a[b[i+1]]:
            ans[b[i]]=match
            c.append(b[i+1])
        else:
            ans[b[i+1]]=match
            c.append(b[i])
    b=c.copy()
    c=[]
    nn=nn//2
    match+=1
  #  print(b)
for i in range(2**n):
    if ans[i]==0:
       # print("RTHN VGHNBGH")
        ans[i]=match-1
    print(ans[i])