n=int(input())
a=list(map(int,input().split()))
count=1
sum1=0
for i in range(n):
    if a[i]==count:
        count+=1
    else:
        sum1+=1
if n==sum1:
    print("-1")
else:
    print(sum1)
    