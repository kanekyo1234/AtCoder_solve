e=list(map(int,input().split()))
a=int(input())
b=list(map(int,input().split()))

ans=0
for i in range(6):
    if e[i] in b:
        ans+=1
if ans==6:
    print("1")
if ans==3:
    print("5")
if ans==4:
    print("4")
if ans==5:
    if a in b:
        print("2")
    else:
        print("3")
if ans<=2:
    print("0")