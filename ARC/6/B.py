from collections import deque
q = deque()
global finished 
finished = set()
c=[]

n,l=map(int,input().split())
for i in range(l+1):
    c.append([" "]+list(map(str,input()))+[" "] )
#for i in range(l+1):
   # print(c[i])
for i in range(n*2+1):
    #print(c[l][i])
    #print(l,i)
    if c[l][i]=="o":
        #print(l,i)
        q.append([l,i])
        



"""
def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False
"""
count=0
def search():
    while (q):
        
        y,x=q.popleft()
        #print(y,x)
        #print(c[y][x])
        
        if c[y][x+1]=="-":
            q.append([y-1,x+2])
        elif c[y][x-1]=="-":
            q.append([y-1,x-2])
        else:
            q.append([y-1,x])
        if y==0:
            if  c[y][x-1]=="-":
                return x-2
            elif c[y][x+1]=="-":
                return x+2
            else:
                return x
ans=search()
#print(ans)
print((ans+1)//2)
"""
幅優先探索

１座標を渡す = 最初の座標をキューに入れる
２そこから行けるところをキューに渡す
３キューからまた取り出す＝１


深さ優先探索
１座標を渡す= 最初の座標をスタックに入れる
２そこから行けるところをスタックに渡す
３スタックからまた取り出す＝１

キューとスタック　　なくなるまで続ける

pop だと深さ優先担ってる
popleftだと幅優先になってる

elif now < n*2 - 2 and amida[i][now+1] == '-':
    これによってlistをはみ出すところを検索していてもindex
    エラーにならないのでわざわざ入力に追加する必要がないと

"""
