n=int(input())
a=list(map(int,input().split()))
c=1#単純増加の数
ans=n#(1,1),(2,2)など
for i in range(n-1):  
    if  a[i]<a[i+1]:
        c+=1   w
    else:
        ans+=c*(c-1)//2  #4C2などの省略
        c=1

ans+=c*(c-1)//2  

print(ans) 