n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]
h.sort()
min1=10**9*1
soezi=0
count=0
for i in range(n-(k-1)):
    count=h[i+(k-1)]-h[i]
    if min1>count:
        min1=count
print(min1)
