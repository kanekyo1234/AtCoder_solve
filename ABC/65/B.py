n=int(input())

a=[int(input()) for _ in range(n)]

count=1
right=a[0]
for i in range(100000+1):
    #print(right,"right")
    if right==2:
        print(count)
        break
    else:
        right=a[right-1]
        count+=1

else:
    print(-1)