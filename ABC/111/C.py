import collections
n=int(input())
v=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,n,2):
    a.append(v[i])
    b.append(v[i+1])
    
a_count=collections.Counter(a)
b_count=collections.Counter(b)



if a_count.most_common()[0][0]==b_count.most_common()[0][0]:
    if a_count.most_common()[0][1]==n//2 :
        print(a_count.most_common()[0][1])
    else:
        print(min(n-a_count.most_common()[0][1]-a_count.most_common()[1][1],n-b_count.most_common()[0][1]-b_count.most_common()[1][1]))
else:
    ans=n-a_count.most_common()[0][1]-b_count.most_common()[0][1]
    print(ans)