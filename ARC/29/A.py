n=int(input())
t=[int(input()) for _ in range(n)]

if n==4:
    t.sort()
    print(min(max(max(t),sum(t)-max(t)),max(max(t)+min(t),sum(t)-max(t)-min(t)),max(t[0]+t[2],t[1]+t[3])))
       # print(max(max(t)+min(t),sum(t)-max(t)-min(t)))

if n==3:
    print(max(max(t),sum(t)-max(t),))
if n==2:
    print(max(t))
if n==1:
    print(sum(t))