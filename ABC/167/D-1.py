import collections
ans=[0,1,2,3,4,5,1,2,3,4,5,6]
ans2=collections.Counter(ans)

ac=ans2.most_common()[0][0]
print(ac)