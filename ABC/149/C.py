x=int(input())
a=0
while a==0:
    count=0
    div=1
    while div<=x:
        if x%div==0:
            count+=1
        div+=1
    if count==2:
        print(x)
        exit()
    x+=1


