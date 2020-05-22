n,m,k=map(int,input().split())

for i in range(n+1):#黒くした行の数
    for j in range(m+1):#黒くした列の数
        #print(i,j,(m*i)+((n-i)*j)-(i*j))
        if (m*i)+((n-i)*j-(i*j))==k:
            print("Yes")
            exit()
print("No")
