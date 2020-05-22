w,h,n=map(int ,input().split())
e = [[int(i) for i in input().split()] for i in range(n)]  
menseki=w*h
h1=h
w1=w
xmax=w
xmin=0
ymax=h
ymin=0

for i in range(n):
    if e[i][2]==1:
        if  xmin<e[i][0] and h>=e[i][0]:
            black=e[i][0] * h1
            menseki-=black
            w1-=e[i][0]   
            xmin=e[i][0] 
    if e[i][2]==2:
        if xmax>e[i][0] and 0<=e[i][0]:
            black=(w-e[i][0]) * h1
            menseki-=black
            w1=(w1-(w-e[i][0]))
            xmax=e[i][0] 
    if e[i][2]==3:
        if  ymin<e[i][1]and w>=e[i][1]:
            black=e[i][1] * w1
            menseki-=black
            h1-=e[i][1]
            ymin=e[i][1]
    if e[i][2]==4:        
        if ymax>e[i][1] and 0<=e[i][1]:
            black=(h-e[i][1]) * w1
            menseki-=black
            h1=(h1-(h-e[i][1]))
            ymax=e[i][1]
if menseki<0:
    print("0")
else:    
    print (menseki)


      