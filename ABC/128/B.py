n=int(input())

data=[list(map(str,input().split())) for _ in range(n)]
#print(data)
for i in range(n):
    data[i][1]=int(data[i][1])*-1
    data[i].append(i+1)

data=sorted(data, key=lambda x:(x[0], x[1]))
for i in range(n):
    print(data[i][2])