n=int(input())
d=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(n):
        if i!=j:
            count+=d[i]*d[j]
count//=2

print(count)
