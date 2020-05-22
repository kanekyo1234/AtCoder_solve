from collections import deque
q = deque()
h,w=map(int,input().split())
sx,sy=1,1#スタート位置
ex,ey=h,w#ゴール位置
q.append([sx-1,sy-1,0])
global finished 
finished = set()
c=[]
for i in range(h):
    c.append(list(map(str,input())))

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False
x
count=0
def search():
    while (q):
        x,y,count=q.popleft()
        
        if check(x,y)==False or (x,y) in finished or c[x][y]=='#':
            continue
        else:
            q.append([x,y-1,count+1])
            q.append([x,y+1,count+1])
            q.append([x+1,y,count+1])
            q.append([x-1,y,count+1])
            finished.add((x,y))
            c[x][y]=count
            if x==ex-1 and y==ey-1:
                return c[x][y]+1 #通った道の合計を返す
    return -1
black_count=0
for i in range(h):
    black_count+=c[i].count("#")
path=search()#通る道
if path==-1:
    print(path)
else:
    print(h*w-black_count-path)#全体からもともと黒の#の数と通った白い道を削除

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

pop だと深さ優先になってる
popleftだと幅優先になってる
"""