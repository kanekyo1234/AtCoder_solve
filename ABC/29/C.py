n=int(input())
pas=['a','b','c']
def dfs(a,ans):
    if a==n:
        print(ans)
        return
    for i in range(3):
        dfs(a+1,ans+pas[i])
  
dfs(0,'')