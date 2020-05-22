n,k=map(int,input().split())

t=[]
for i in range(n):
    t.append(list(map(int,input().split())))

def dfs(val,ans):
    #print(val,ans)
    if val==n:

        if ans==0:#XORが0ならTrueでこの再起から抜ける
            return True
        else:
            return False
    for i in range(k):
        if dfs(val+1,ans^t[val][i]):#Trueなら
            return True
    return False
if dfs(0,0):#Trueなら
    print("Found")
else:
    print("Nothing")