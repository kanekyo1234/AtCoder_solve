n,x,y=map(int,input().split())
adlist=[[1,2]]
for i in range(n-2):
    adlist.append([i+1,i+2,i+3])
adlist.append([n-1,n])

adlist[x-1].append(y)
adlist[y-1].append(x)


def dfs(start,count,goal,finish,ans):
    finish.add(start)#もう訪れたところ
   
   # print(finish)
    if count==goal:
        #print("DFGH")
        ans+=1
        #print(ans)
        count=0
    for i in adlist[start-1]:
        #print("DFG")
        if i not in finish:#通ったところに入っていないなら通れるということ   
            #print(i)
            dfs(i,count+1,goal,finish,ans)
    return ans

#print(adlist)
global ans
for i in range(1,n):
    
    ans=0
    finish=set()
    print(dfs(1,0,i,finish,0))

#print(adlist)