n,k=map(int,input().split())
a=n%k
if n<k:
    print(min(n,abs(n-k)))
    exit()

if n%k==0:
    print(0)
else:
    print(min(k-a,a))