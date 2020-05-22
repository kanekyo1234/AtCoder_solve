x,y,r=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())

#資格が隠れるか

#print(ax1,ax2,ay1,ay2)
bx1=x-r
bx2=x+r
by1=y-r
by2=y+r

def jugh(x,y):
    #print(x,y,x**2+y**2)
    if x**2+y**2<=r**2:
        #print("HJK")
        return True
    else:
        #print(" BNM")
        return False

if jugh(x-x1,y-y1) and  jugh(x-x1,y-y2) and  jugh(x-x2,y-y1) and  jugh(x-x2,y-y2) :
    print("YES")
    print("NO")


elif  x1<=bx1 and bx2<=x2 and y1<=by1 and by2<=y2:
    print("NO")
    print("YES")

else:
    print("YES")
    print("YES")