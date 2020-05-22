n=int(input())
d=[0]*n
for i in range(n):
    d[i] = list(map(str,input().split()))
q=int(input())
p=[]
for i in range(q):
    p.append(int(input()))

nizyou=[]
for i in range(1,n+1):
    nizyou.append(i*i)
print(nizyou)


count=0
for i in range(n+1):
    for j in range(i,n+1):
        count+=1
print(count)

