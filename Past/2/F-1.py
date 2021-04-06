import heapq
n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ok=0 #kが超えない大丈夫なとこまで
ab=sorted(ab, key=lambda x:(x[0], -x[1]))

for i in range(n):
    ab[i][1]*=-1#ヒープは最小の値を高速に出してくれるのですべてにマイナスを懸けて最大値を最小値にする
    

count=0
ans=[0]
for i in range(1,n+1):
    while ok<n:
        if ab[ok][0]==i:
            heapq.heappush(ans,ab[ok][1])
            ok+=1
        else:
            break
    #print(ans)
    count-=heapq.heappop(ans)
    print(count)