n, m = map(int, input().split())
a = list(map(int, input().split()))
L = 0
R = 10**9+1
now = [0]
start=0

for i in range(m):
    if len(now) == 3:
        break
    start+=1
    for j in range(len(now)):
        if now[j] < a[i]:
            now[j] = a[i]
            print(j+1)
            break
    else:
        if n-len(now)!=0:
            now.append(a[i])
            print(len(now))
        else:
            print(-1)
else:
    exit()
#print(start,now)
print()

def ans(center):
    return now[center]

#print(now)
for i in range(start,m):
    L = 0
    R = len(now)-1#index
    x = a[i]
    center = (R+L)//2
    count = ans(center)
    while R-(L+1) > 0:
        center = (R+L)//2
        count = ans(center)
        if x >= count:
            R = center
        else:
            L = center
    #print(center,L,R,a[i])
    if now[L]<a[i]:
        now[L]=a[i]
        print(L+1)
    elif now[R]>=a[i]:
        if R==len(now)-1:
            if n-len(now)!=0:
                    now.append(a[i])
                    print(R+2)
            else:
                print(-1)
        else:
            now[R+1]=a[i]
            print(R+2)
    else:
        now[L+1]=a[i]
        print(L+2)
   ## print(now)

#print(now)
