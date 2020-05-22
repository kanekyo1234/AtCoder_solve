a,b,k,l=map(int,input().split())

if a*l <= b:#セットとの値段の確認
    print(k*a)
else:
    ans=k//l*b
    print(min(ans+b,ans+k%l*a))