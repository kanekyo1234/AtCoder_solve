
a,b,c=map(int,input().split())

if c-a-b<0:
    print("No")
elif 4*a*b<(c-a-b)**2:#式変形桁落ちはわかっていたが式変形のかんがえかたがなかった
    print("Yes")
else:
    print("No")
