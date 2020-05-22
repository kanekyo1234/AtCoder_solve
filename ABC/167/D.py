import collections
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
now=0
for i in range(n+1):
        ans.append(a[now])
        now=a[now]-1
#print(ans)

ans2=collections.Counter(ans)

ac=ans2.most_common()[0][0]
#print(ac)
index=-1
index2=-1

for i in range(len(ans)):
    if ans[i]==ac:
        if index==-1:
            
            index=i
        else:
            index2=i

print(index,index2)
print((k-index-1)%(index2-index))

print(ans[(k-index-1)%(index2-index)+index])
"""

n,k = map(int,input().split())
a = list(map(int,input().split()))
cnt = 1
next = a[0]
tmp_list = [a[0]]
roop_list = []
tmp_set = set([a[0]])
while(True):
    next = a[next-1]
    if next in tmp_set:
        hajimari = tmp_list.index(next)
        roop_list = tmp_list[hajimari:]
        cnt -= hajimari
        break
    tmp_set.add(next)
    tmp_list.append(next)
    cnt +=1
print(roop_list[((k-hajimari)%cnt)-1])
"""