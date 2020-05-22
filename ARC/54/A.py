l,x,y,s,d=map(int,input().split())

tokei=(d-s+l)%l/(x+y)
if x>=y:
    print(tokei)
    exit()
re_tokei= (s-d+l)%l/(y-x)
print(min(tokei,re_tokei))