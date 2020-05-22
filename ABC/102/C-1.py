import collections
n=int(input())

a=list(map(int,input().split() ))
absa=[]
za=[]

for i in range(n):
    za.append(a[i]-(i+1))


c = collections.Counter(za)

if c.most_common()[0][1]==1:
    b=c[i]
else:
    b=c.most_common()[0][0]

for i in range(n):
    absa.append(abs(a[i]-(b+(i+1))))



#print(absa)
print(sum(absa))
