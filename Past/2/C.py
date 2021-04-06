n=int(input())
s=[]
for i in range(n):
    s.append(list(str(input())))
a=set()
ans=[[0]*(n*2-1) for _ in range(n)] 

for i in range(n-1,-1,-1):
    for h in range(n*2-1):
        if h in a and s[i][h]!=".":
           # print("DFGhj")
            ans[i][h]="X"
        else:
            ans[i][h]=s[i][h]
    #print(ans)
    a=set()
    for j in range(n*2-1):
        if ans[i][j]=='X':
            a.add(max(0,j-1))
            a.add(j)
            a.add(min(n*2-1,j+1))
   # print(a)

for i in range(n):
    for j in range(n*2-1):
        print(ans[i][j],end="")
    print()