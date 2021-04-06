n=int(input())

a=list(map(int,input().split()))
finish=[]
for i in range(n):
    start=i
    now=i
    count=1
    for j in range(n):
        now=a[now]-1
        if now==start:
            print(count,end=" ")
            break
        else:
            count+=1

