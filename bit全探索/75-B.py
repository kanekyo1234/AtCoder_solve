from itertools import  product
h,w=map(int,input().split())

s=[]
for i in range(h):
    s.append(list(map(str,input())))

#print(s)
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            print(s[i][j],end="")
        else:
            count=0
            for z in product((0, 1, -1), repeat=2):
                x,y=z
                
                if x!=0 or y!=0:
                    if 0<=(i-x) and (i-x)<h and 0<=(j-y) and (j-y)<w and s[i-x][j-y]=='#':
                        count+=1
            print(count,end="")
    print()

