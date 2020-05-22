n=int(input())
ans=0
if n==1:
    print(1)
    exit()


for i in range(n):
    for j in range(2,11):
        if i**j<=n:
           ans=max(ans,i**j) 
print(ans)