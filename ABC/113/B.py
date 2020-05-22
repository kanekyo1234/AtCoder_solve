n=int(input())
t,a=map(int,input().split())

h=list(map(int,input().split()))

ans=[]

for i in range(n):
    ans.append(abs(a-(t-h[i]*0.006)))

print(ans.index(min(ans))+1)