import collections
n=int(input())
a=list(map(int,input().split() ))
absa=[]
za=[]
for i in range(n):
    za.append(a[i]-(i+1))
#print(za)
#print(sum(za))
za.sort()
if n%2==1:
    b=za[n//2]
else:
    b=(za[n//2-1]+za[n//2])//2

#print(b)
for i in range(n):
    absa.append(abs(a[i]-(b+(i+1))))
#print(absa)
print(sum(absa))
