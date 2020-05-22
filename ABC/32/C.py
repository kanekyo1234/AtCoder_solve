n,k=map(int,input().split())#多分尺取り
s=[int(input()) for _ in range(n)]
if 0 in s:
    print(n)
    exit()
start=0
goal=0
count=s[0]

ans=0

while goal<n :
    #print(count,goal,start)
    if count<=k:
        
        ans=max(ans,(goal-start+1))
        goal+=1
        count*=s[min(n-1,goal)]
    else:
        if goal!=start:
            count=count//s[min(n-1,start)]
            start+=1
        else:
            goal+=1
            start+=1
            count=s[min(n-1,start)]
print(ans)
    


    