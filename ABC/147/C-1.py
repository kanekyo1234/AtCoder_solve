#ゆうたのやり方

n=int(input())
xy=[[] for i in range(n)]

for i in range(n):
    a=int(input())
    for j in range(a):
        xy[i].append(list(map(int, input().split())))
#print(xy)
bit=[]#1が正直0が嘘
ans=0
def bit_search(bit):
    global ans
    if len(bit)==n:#2**n文の組み合わせを調べる加圧10を交互に入れるためのif
        for i in range(n):
            
            jugh=bit[i]
            if jugh==1:#0(嘘)の時はやる必要がない
                for j in xy[i]:
                    x,y=j
                    if bit[x-1]==0:#ここら辺はbit[1]が１の時に0だって証言があったらだめだからreturnするって感じ
                        if y==1:
                            return 
                    else:
                        if y==0:
                            return 
                            
        ans=max(ans,sum(bit))
    else:
       #再起化することによって最初にbitの配列を作る必要性をなくした
        bit_search(bit+[0])
        bit_search(bit+[1])
bit_search(bit)
print(ans)