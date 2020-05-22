n=int(input())
print(ord("a"))
def dfs(ans):
    if n==len(ans):
        print(ans)
    else:
        print(ans)
        for i in range(int(ord("a")),int(ord(ans))):
            dfs(ans+chr(i+1))#条件式

dfs("a")
