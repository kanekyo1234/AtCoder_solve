a=int(input())
b=list(map(int,input().split()))
b.append(b[-1])
c=[b[0]]

for i in range(1,a):
    c.append(min(b[i],b[i-1]))

ans=sum(c)
print(ans)
