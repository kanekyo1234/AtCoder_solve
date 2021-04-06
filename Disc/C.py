h,w,k = map(int,input().split())
e = [[str(i) for i in input()] for i in range(h)] 
count=1
for i in range(h):
    for j in range(w):
        if e[i][j] in "#"and j==w-1 and e[i][j-1]=="#" :
            
            count+=1
            e[i][j]=count
        elif     e[i][j] in "#"and j==w-1:
            e[i][j]=count
            count+=1
        elif e[i][j] in "#":
            
            e[i][j]=count
            count+=1
        elif j==w-1:
            e[i][j]=count
            count+=1
        else:
            e[i][j]=count
for i in range(h):
    for j in range(w):
        print(e[i][j])
    