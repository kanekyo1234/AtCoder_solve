n=int(input())
imos=[0]*1000002
for i in range(n):
    a,b=map(int,input().split())
    imos[a]+=1#出発点
    imos[b+1]-=1 #到着店の一個先
#print(imos)
for i in range(1,1000001):
    imos [i]+=imos[i-1]
print(max(imos))