h,w=map(int,input().split())

if h%3==0 or w%3==0:
    print("0")
    exit()
#print(h*w)
ans=10**100**2
    #hが大きい方とみなす
if h<w:
    comp=h
    h=w
    w=comp
ans=min(ans,(h//3+1)*w-h//3*w)
#縦に三等分に分けるやりかや　5　11を試す

#print(ans)
#print(h*w)
for i in range(1,w):
    green = h*i 
    red   = (h//2) * (w-i)
    blue  = h*w-red-green#三等分に分ける
    #print(green,red,blue)
    ma=max(green,red,blue)#一番大きい長方形
    mi=min(green,red,blue)#一番小さい長方形
    #print(green,red,blue,ma-mi)
    ans=min(ans,ma-mi)
#縦横横に分けるやり方を縦横でためす　


comp=w
w=h
h=comp
for i in range(1,w):
    green = h*i 
    red   = (h//2) * (w-i)
    blue  = h*w-red-green#三等分に分ける
    ma=max(green,red,blue)#一番大きい長方形
    mi=min(green,red,blue)#一番小さい長方形
    #print(green,red,blue,ma-mi)
    ans=min(ans,ma-mi)

print(ans)