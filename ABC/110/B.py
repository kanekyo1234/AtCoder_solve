n,m,X,Y=map(int,input().split())

x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(X+1,Y+1,1):
    if max(x)<i and i<=min(y):
        print("No War")
        exit()
print("War")