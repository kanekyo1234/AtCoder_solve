import collections

a=[str(i) for i in input()]
c=collections.Counter(a)
if c.most_common()[0][1]>=2:
    print("no")
else:
    print("yes")