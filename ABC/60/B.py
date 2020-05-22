a,b,c=map(int,input().split())


for i in range(1,100000):
    if (a+(a*i))%b==c:
        print("YES")
        break
else:
    print("NO")