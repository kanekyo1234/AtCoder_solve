n,t=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
a=[]
b=[]


for i in range(n):
    ab[i].append(ab[i][0]-ab[i][1])
    a.append(ab[i][0])
    b.append(ab[i][1])
suma=sum(a)
sumb=sum(b)
ab_sort=sorted(ab, key=lambda x:(x[2], x[0]),reverse=True)

for i in range(n):
    if t<suma:
     #   print(suma)
        suma-=ab_sort[i][2]
    else:
        print(i)
        break
else:
    if t<suma:
        print(-1)
    else:
        print(n)
#print(ab_sort)