a=[]
for i in range(3):
    a.append(list(map(int,input().split())))

n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))

ans=[[0 for i in range(3)] for i in range(3)]

for z in range(n):
    for i in range(3):
        for j in range(3):
            if a[i][j]==b[z]:
                ans[i][j]=1

#print(ans)
c=0
for i in range(3):
    if ans[0][i]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0
for i in range(3):
    if ans[1][i]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0 
for i in range(3):
    if ans[2][i]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0  
for i in range(3):
    if ans[i][0]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0  
for i in range(3):
    if ans[i][1]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0   
for i in range(3):
    if ans[i][2]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0  
for i in range(3):
    if ans[1][i]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0

for i in range(3):
    if ans[i][i]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0

for i in range(3):
    if ans[2-i][i]==1:
        c+=1
if c==3:
    print("Yes")
    exit()
c=0
print("No")