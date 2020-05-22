n=int(input())
a=list(map(int,input().split()))

count=0
for i in range(n):
    count+=1/a[i]
print(1/count)