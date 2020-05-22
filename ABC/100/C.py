n=int(input())
a=list(map(int,input().split()))
ans=0

def cnt(x):
    if x%2==1:
        return 0
    else:
        return cnt(x//2)+1
for i in range(n):
    ans+=cnt(a[i])
print(ans)