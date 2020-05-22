n=int(input())
a=[]

for i in range(n):
    a.append(int(input()))

zisyo={}
for i in range(n):
    if a[i] in zisyo:
        zisyo.pop(a[i])
    else:
        zisyo[a[i]]=1
print(len(zisyo))