n,m=map(int,input().split())
k=[]
zisyo={}

for i in range(n):
    k.append(list(map(int,input().split())))

for i in range(n):
    for j in range(1,k[i][0]+1):
        if  str(k[i][j]) in zisyo:
            zisyo[str(k[i][j])]+=1
        else:
            zisyo[str(k[i][j])]=1

count=0

for key,val in zisyo.items():
    if val==n:
        count+=1
print(count)