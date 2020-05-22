n,k=map(int,input().split())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))


a.sort()
#print(a)
count=0
i=0
while count<k:
    count+=a[i][1]
    i+=1

print(a[i-1][0])