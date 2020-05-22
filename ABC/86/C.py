n=int(input())

t=[]
x=[]
y=[]

for i in range(n):
    a,b,c=map(int,input().split())
    t.append(a)
    x.append(b)
    y.append(c)
for i in range(n):
    if x[i]+y[i]>t[i] or (x[i]+y[i])%2!=t[i]%2:
        print("No")
        exit()

print("Yes")
        