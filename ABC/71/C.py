"""import collections
n=int(input())
a=list(map(int,input().split()))
ac=collections.Counter(a)

for k,i in ac.items():
"""
n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
count=0
ans4=0
ans2=[0]*2
for i in range(n-1):
    #print(a[i],i)
    if a[i]==a[i+1]:
        count+=1
    if i==(n-2) or a[i]!=a[i+1]:
        if 1<=count:
            if 3<=count:
                ans4=max(ans4,a[i])
                ans2.append(a[i])
            else:
                ans2.append(a[i])
        count=0
ans2.sort(reverse=True)
#print(ans2)  
print(max(ans4**2,ans4*ans2[0],ans2[0]*ans2[1]))