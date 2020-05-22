n,y=map(int,input().split())
if y>10000*n:
    print("-1 -1 -1")
else:
    for i in range(n+1):
        #print(i)
        for j in range(n-i+1):
            if y==10000*i+5000*j+(n-i-j)*1000:
                print(i,j,(n-i-j))
                exit()
    print("-1 -1 -1")