n=int(input())
a=[ str(input())[::-1] for _ in range(n)]

a.sort()
for i in range(n):
    print(a[i][::-1])