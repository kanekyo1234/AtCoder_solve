r,c,d=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(r)]
ans=0
count=0
if d%2==0:
    for i in range(0,r):
        for j in range(i%2,min(c,d+1-i),2):
            ans=max(ans,a[i][j])
     
    print(ans)



else:
    for i in range(0,r):
      #  print(min(c,d+1-i))
        for j in range((i+1)%2,min(c,d+1-i),2):
          #  print(a[i][j],i,j)
            ans=max(ans,a[i][j])
   # print()
    print(ans)
    