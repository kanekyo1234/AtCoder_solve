from collections import deque
q = deque()
h,w=map(int,input().split())
global finished 
finished = set()
c=[]

for i in range(h):
    c.append( list(map(str,input())))


for i in range(h):
    for j in range(w):
        if c[i][j]=='s':
            q.append([i,j])

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False


while (q):
    x,y=q.popleft()
    if check(x,y)==False or (x,y) in finished or c[x][y]=='#':
       
        continue
    else:
        if c[x][y]=='g':
            print("Yes")
            exit()
        q.append([x,y-1])
        q.append([x,y+1])
        q.append([x+1,y])
        q.append([x-1,y])
        finished.add((x,y))
print("No")

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

"""