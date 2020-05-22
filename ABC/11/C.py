
n=int(input())
ng=[]
for i in range(3):
    ng.append(int(input()))
if n in ng :
    print("NO")
    exit()
for i in range(100):
    c=3#引く値
    if n-3 in ng:
        if n-2 in ng:
            if n-1 in ng:
                print("NO")
                exit()
            else:
                c=1
        else:
            c=2
    n-=c
if n<=0:
    print("YES")
else:
    print("NO")

    