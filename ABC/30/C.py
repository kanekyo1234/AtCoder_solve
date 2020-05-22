n,m=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a_count=0
b_count=0
count=0#到着回数
now=0#現在地

while True:
    for i in range(a_count,n):
        if now<=a[i]:
            now=a[i]+x
            a_count=i+1
            count+=1
            #print("a")
            break
    else:
        print(count//2)
        exit()


    for i in range(b_count,m):
        if now<=b[i]:
            now=b[i]+y
            b_count=i+1
            count+=1
            #print("b")
            break
    else:
        print(count//2)
        exit()
