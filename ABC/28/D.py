n,k=map(int,input().split())
ans=0
#kが何個あるかで分けて考える

ans+=(k-1)*(n-k)*6

ans+=(n-1)*3

ans+=1

print(ans/(n**3))