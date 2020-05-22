import heapq
n,m,v,p=map(int,input().split())
a=list(map(int,input().split()))

a=[-1*i for i in a]#最大値をとるため＊－１
heapq.heapify(a)
maxa=heapq.heappop(a)*-1
a=[-1*i for i in a]#最大値をとるため＊－１
heapq.heapify(a)

h=maxa-m
count=0
for i in range(n):
    ma=heapq.heappop(a)
    if ma>=h:
        break
    count+=1
    heapq.heappush(a,maxa)
print(n-count)