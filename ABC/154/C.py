n=int(input())
a=list(map(int,input().split()))
c=set(a)
if len(a)==len(c):
    print("YES")
else:
    print("NO")
