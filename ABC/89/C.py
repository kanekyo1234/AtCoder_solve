import itertools 
n=int(input())
a=[]
for i in range(n):
    a.append(str(input()))
march=[0]*5
for i in range(n):
    if as[i][0:1]=='M':
        march[0]+=1
    if a[i][0:1]=='A':
        march[1]+=1
    if a[i][0:1]=='R':
        march[2]+=1
    if a[i][0:1]=='C':
        march[3]+=1
    if a[i][0:1]=='H':
        march[4]+=1
#三人を選ぶほうほうのそれぞれのかずを懸けあわっせる
#print(march)
kumi_list=list(itertools.combinations([0,1,2,3,4],3))
#print(kumi_list)
ans=0
for i in kumi_list:
    b,c,d= i
    #print(b,c,d) 
    ans+=march[b]*march[c]*march[d]
print(ans)
