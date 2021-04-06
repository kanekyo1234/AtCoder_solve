from collections import deque

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False

def G_shap():#＠を#に変える関数
    while (S):
        x,y,count=S.popleft()
        
        if check(x,y)==False or (x,y) in finishedS or c[x][y]=='#':#イノシシも通れないため＃の場所はそもそもカウントしない
            continue
        else:
            if c[x][y]!='S'  :#Sのところはけさない
                if count==0 or  c[x][y]!='@':#＠が重複してるところが消えるのを防ぐ
                    c[x][y]='#'
            if  count>=d:#入力で指定されている階数より上のところはいかないようにセッティング
                continue
            else:
                S.append([x,y-1,count+1])
                S.append([x,y+1,count+1])
                S.append([x+1,y,count+1])
                S.append([x-1,y,count+1])
                finishedS.add((x,y))

def search():
    while (q):
        x,y,count=q.popleft()
        
        if check(x,y)==False or (x,y) in finisheds or c[x][y]=='#':
            continue

        else:
            q.append([x,y-1,count+1])
            q.append([x,y+1,count+1])
            q.append([x+1,y,count+1])
            q.append([x-1,y,count+1])
            finisheds.add((x,y))
            if c[x][y]=='G':
                return count
            else:
                c[x][y]=count
    return -1
        


q = deque()
S = deque()#@を#にするため
h,w,d=map(int,input().split())
global finisheds 
global finishedS 
finisheds = set()
finishedS = set()#@を#にするため
c=[]
for i in range(h):
    c.append(list(map(str,input())))

for i in range(h):
    for j in range(w):
        if c[i][j]=='S':
            q.append([i,j,0])
        if c[i][j]=='@':
            S.append([i,j,0])
            G_shap()
"""  
for i in range(h):
    print(c[i])
"""
print(search())

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

"""