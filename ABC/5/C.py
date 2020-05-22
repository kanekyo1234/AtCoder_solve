t=int(input())
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

if n<m:
    print("no")
    exit()


count=0
for i in range(m):
    jagh=0
    while (jagh!=1):
        if count>=n:
            print("no")
            exit()
        if b[i]>=a[count] and b[i]<=a[count]+t:
            jagh=1
            count+=1
        else:
            count+=1

print("yes")