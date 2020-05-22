from itertools import  product
import copy
h,w=map(int,input().split())

s=[list(str(input())) for _ in range(h)]
ans=[[0]*w for _ in range(h)]

def check(x,y):
    if 0<=x and x<h:
        if 0<=y and y<w:
            return True
    return False

for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            for z in product((0, 1,-1), repeat=2):
                x,y=z
                if x==0 and y==0:
                    continue
               # print(i+x,j+y)
                if check(i+x,j+y)==True and s[i+x][j+y]=='.':#ダメな時＝check関数内に入っているかつ＃出ない
                    ans[i][j]='.'
                    break
            else:
                ans[i][j]='#'

        else:
            ans[i][j]='.'

ans2=copy.deepcopy(ans)#値私をしないといかん　二次元配列なので深いコピーな


for i in range(h):
    for j in range(w):
        if ans2[i][j]=='#':
            for z in product((0, 1,-1), repeat=2):
                x,y=z
                if x==0 and y==0:
                    continue
               # print(i+x,j+y)
                if check(i+x,j+y)==True and ans2[i+x][j+y]!='#':
                    ans2[i+x][j+y]='1'

for i in range(h):
    for j in range(w):
        if ans2[i][j]=='1':
            ans2[i][j]='#'
"""
print()
for i in range(h):
    print(s[i])
print()
for i in range(h):
    print(ans[i])
print()
for i in range(h):
    print(ans2[i])
print()
"""

for i in range(h):
    for j in range(w):
        if ans2[i][j]!=s[i][j]:
            print("impossible")
            exit()

print("possible")
for i in range(h):
    for j in range(w):
        print(ans[i][j],end="")
    print()