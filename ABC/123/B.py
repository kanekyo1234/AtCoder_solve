a=[int(input()) for _ in range(5)]
ans=sum(a)
b=10
for i in range(5):
    if a[i]%10!=0:
        ans+=10-a[i]%10
        b=min(b,a[i]%10)
print(ans-10+b)