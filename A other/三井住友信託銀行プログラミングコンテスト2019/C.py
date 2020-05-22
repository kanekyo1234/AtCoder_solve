a=int(input())
if a>=2100:
    print("1")
else:
    b=a//100#20
    c=a%100 #amari
    for i in range(b):
        c-=5
    if c>0:
        print ("0")
    else:
        print("1")
        