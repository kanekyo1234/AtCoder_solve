h,w=map(int,input().split())
s=[]
s.append(['.']*(w+2))
for i in range(h):
    s.append( list(map(str,input())))
    

s.append(['.']*(w+2))
for i in range(1,h+1):
    s[i].insert(0,'.')
    s[i].append('.')


for i in range(1,h):
    for j in range(1,w):
        if s[i][j]=='#':
            if s[i+1][j]!='#' and s[i-1][j]!='#' and s[i][j+1]!='#' and s[i][j-1]!='#' :
                print("No")
                exit()

print("Yes")