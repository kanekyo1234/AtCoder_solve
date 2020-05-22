n=int(input())
aas=list(map(int,input().split()))
a=[]

for i in range(n):
    a.append([i+1,aas[i]])
#print(a)
a.sort(key=lambda x:x[1] , reverse=True)
for i in range(n):
    print(a[i][0])