c=int(input())
nml=[sorted(list(map(int,input().split()))) for _ in range(c)]
n=[]
m=[]
l=[]

for i in range(c):
    n.append(nml[i][0])
    m.append(nml[i][1])
    l.append(nml[i][2])
    
print(max(n)*max(m)*max(l))