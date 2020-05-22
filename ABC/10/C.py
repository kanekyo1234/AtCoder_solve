txa,tya,txb,tyb,t,v=map(int,input().split())
n=int(input())
range_rode=t*v
xy=[]
for i in range(n):
    xy.append(list(map(int,input().split())))

for i in range(n):
    x,y=xy[i]
    #print(y)
    road=((x-txa)**2+(y-tya)**2)**0.5+((txb-x)**2+(tyb-y)**2)**0.5
    #print(road)
    if road <= range_rode:
        print("YES")
        break
else:
    print("NO")
