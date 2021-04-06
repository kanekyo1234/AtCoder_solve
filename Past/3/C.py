a,r,n=map(int,input().split())
if r==1:
    print(a)
    exit()
count=a
for i in range(n-1):
    
    if 10**9<(count*r):
        print("large")
        break
    count=count*r
else:
    print(count)