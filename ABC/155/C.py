import collections

n=int(input())

s=[]
for i in range(n):
    s.append(str(input()))

scount=collections.Counter(s)
#print(scount[1][1])
maxc=scount.most_common()[0][1]
#print(maxc)
ans=[]
for k, v in scount.items():
    if v==maxc:
        ans.append(k)


ans.sort()
for i in range(len(ans)):
    print(ans[i])
