n=int(input())
x=[]
y=[]
h=[]
xyh=[list(map(int,input().split())) for _ in range(n)]
xyh.sort(reverse=True ,key=lambda na:(na[2]))#最初に高さが0だと間違いになるからこれがいる
#print(xyh)
for i in range(n):
    x.append(xyh[i][0])
    y.append(xyh[i][1])
    h.append(xyh[i][2])

#print(h)
#中心座標を列挙
for i in range(101):#x
    for j in range(101):#y
        ha=abs(i-x[0])+abs(j-y[0])+h[0]
        for z in range(1,n):#違うかの確かめ作業
            if h[z] != max(ha-abs(i-x[z])-abs(j-y[z]),0):
                break
        else:
            print(i,j,ha)
            exit()
#print("DFGH")



