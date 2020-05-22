n=int(input())
ab=[]
cd=[]
for i in range(n):
    ab.append(list(map(int,input().split())))
    

for i in range(n):
    cd.append(list(map(int,input().split())))

cd.sort()
ab.sort(key=lambda x:x[1])
#print(ab,cd)
ans=0
for i in range(n):
    for j in range(len(cd)):
        if ab[i][0]<cd[j][0] and  ab[i][1]<cd[j][1] : 
            
            ans+=1
            cd.pop(j)
            #print(ab,cd)
            break
print(ans)