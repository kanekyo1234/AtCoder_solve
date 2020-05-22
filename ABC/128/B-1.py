n=int(input())
sp=[list(map(str,input().split())) for _ in range(n)]
for i in range(n):
    sp[i].append(i+1)
    sp[i][1]=int(sp[i][1])
sp=sorted(sp, key=lambda x:(x[0], -x[1]))

for i in range(n):
    print(sp[i][2])
