n=int(input())

h=list(map(int,input().split()))

for i in range(n-2):
    if h[i+1]-h[i]>=2:
        print("No")
        break
    else:
        if h[i]<h[i+i]:
            h[i+1]-=1
else:
    if h[-2]<=h[-1]:
        print("Yes")
    else:
        print("No")
