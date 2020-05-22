n,m=map(int,input().split())
a=[list(str(input())) for _ in range(n)]
b=[list(str(input())) for _ in range(m)]
            
#print(a,b)

for i in range(n-m+1):#二回
    for j in range(n-m+1):#二回
        jugh=True
      #  print(i,j)
        for x in range(m):
            for y in range(m):
         #       print(x,y)
                if a[x+i][y+j]!=b[x][y]:
                    jugh=False
                   # print(x,y)
                    break
        if jugh==True:
            print("Yes")
            exit()

print("No")