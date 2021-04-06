n=int(input())
a=[int(input()) for i in range(n)]
a.insert(0,0)
a.sort()
huk=0
nasi=n
for i in range(n):
    if a[i+1]-a[i]==0:
        huk=a[i+1]
    elif a[i+1]-a[i]==2:
        nasi=(a[i+1]+a[i])//2

if huk!=0:
    print(huk,end=" ")
    print(nasi)
else:
    print("Correct")
