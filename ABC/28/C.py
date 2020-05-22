a=list(map(int,input().split()))
ans=[]

for i in range(3):
    for j in range(i+1,4):
        for z in range(j+1,5):
            ans.append(a[i]+a[j]+a[z])
ans.sort()
print(ans[-3])