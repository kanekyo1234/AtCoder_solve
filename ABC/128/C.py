from itertools import  product

n,m=map(int,input().split())

ks=[ list(map(int,input().split())) for _ in range(m) ]

p=list(map(int,input().split()))
ans=0

for z in product((0, 1), repeat=n):#bit全探索のくみあわせ
    for i in range(m): #ついてるスイッチと入力が正しいかの判定ループ
        k=ks[i][0]#
        on_count=0#
        for j in range(1,k+1):##組み合わせと比較をm回分やる
            if z[ks[i][j]-1]==1:#組み合わせと比較
                on_count+=1
        if  on_count%2!=p[i]:#pとついてるスイッチの個数%２が会わなかったらループ終了
            break

    else:#上のループでbreakしなかったら（この条件を通る）すべて正解といううことなのでans+1
        ans+=1
print(ans)   
#print(z)
