a=int(input())
b=list(input())
count=0
if a%2==1:
    print("No")
else:
    for i in range(0,a//2,1):
        if b[i]!=b[i+a//2]:
            count+=1
    if count==0:
        print("Yes")
    else:
        print("No")