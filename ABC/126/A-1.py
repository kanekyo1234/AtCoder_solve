n,k=map(int,input().split())
a=list(str(input()))
a[k-1]=chr(ord(a[k-1])+32)

for i in range(n):
    print(a[i],end="")
