n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(1,n):
    #print(a)
    if a[i-1]<0:
        if 0<a[i]:
            a[i]=a[i-1]+a[i]
            print(a)
        else:#両方-だったら
            if a[i-1]<a[i]:
                a[i]+=abs(a[i])+1
                count+=abs(a[i])+1
            else:
                a[i-1]+=abs(a[i-1])+1
                count+=abs(a[i-1])+1
            print(a)
            a[i]=a[i-1]+a[i]
    else:#"0<a[i-1]"
        if a[i]<0:
            a[i]=a[i-1]+a[i]
            print(a)
        else:#両方+だったら
            if a[i-1]<a[i]:
                a[i-1]-=abs(a[i-1])+1
                count+=abs(a[i-1])+1
            else:
                a[i]-=abs(a[i])+1
                count+=abs(a[i])+1
            print(a)
            a[i]=a[i-1]+a[i]
    print(a)
    print(count)
