n=int(input())

d=[int(input()) for _ in range(n)]

d.sort()
d=set(d)
print(len(d))