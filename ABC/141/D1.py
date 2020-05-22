import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))

a=[-1*i for i in a]#最大値をとるため＊－１
heapq.heapify(a)#二分木の形にする
for i in range(m):#ｍ回
    ma=heapq.heappop(a)#listから最小（最大）を取り出しその値を記憶するためのma
    ma*=-1#-のままだと-3//2=2になってしまうので計算が合わない
    heapq.heappush(a,-1*(ma//2))#2で割った値に－１を懸けて戻す
print(sum(a)*-1)#https://qiita.com/T_Wakasugi/items/dac6eb77a3cace54f95e

