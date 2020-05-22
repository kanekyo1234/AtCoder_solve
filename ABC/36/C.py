n=int(input())
a=[int(input()) for _ in range(n)] 


b=set(a)
b=sorted(b)
#print(b)
zisyo={}
for i in range(len(b)):
    zisyo[b[i]]=i
#print(zisyo)
for i in range(n):
    print(zisyo[a[i]])

