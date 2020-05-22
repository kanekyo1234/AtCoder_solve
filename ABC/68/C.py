m,n=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

dep = []#一個目のの到着場所
arr = []#二回目のの出発場所
for i in range(n):
    if a[i][0]==1:
        dep.append(a[i][1])
    if a[i][1]==m:
        arr.append(a[i][0])
dep=set(dep)
arr=set(arr)
ans=dep & arr

if len(ans)==0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")