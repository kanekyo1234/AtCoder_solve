a,b,c=map(int,input().split())

k=int(input())

d=max(a,b,c)
for i in range(k):
    d*=2
print(a+b+c-max(a,b,c)+d)