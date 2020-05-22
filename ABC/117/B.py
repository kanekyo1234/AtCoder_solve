n=int(input())
l=list(map(int,input().split()))

l.sort(reverse=True)
if l[0]<sum(l)-l[0]:
    print("Yes")
else:
    print("No")