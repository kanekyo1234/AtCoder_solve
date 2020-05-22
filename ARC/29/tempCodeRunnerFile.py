n=int(input())
t=[int(input()) for _ in range(n)]

if n==4:
    print(min(max(t)+min(t),sum(t)-max(t)-min(t)))
if n==3:
    print(min(max(t),sum(t)-max(t))
if n==2:
    print(min(t))
if n==1:
    print(sum(t))