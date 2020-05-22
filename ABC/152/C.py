n=int(input())
p=list(map(int,input().split()))
mina=10**10
count=0
for i in range(n):
    if mina>p[i]:
        mina=p[i]
        count+=1

print(count) 