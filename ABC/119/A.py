a=list(map(int,input().split('/')))
#print(a)
if a[0]==2019:
    if a[1]==4:
        if 30>=a[2]:
            print("Heisei")
        else:
            print("TBD")
    elif 5>a[1]:
        print("Heisei")
    else:
        print("TBD")
elif 2019>=a[0]:
    print("Heisei")
else:
        print("TBD")