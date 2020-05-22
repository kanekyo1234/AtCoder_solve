a,b=map(int,input().split())
ans=10000
for i in range(a,b):
    for j in range(i+1,b+1):
        if i>=2019:
            i=i%2019
        if j>=2019:
            j=j%2019
        if i==0 or j==0:
            print("0")
            exit()
        else:
            if ans>i*j%2019:
                ans=i*j%2019
print(ans)