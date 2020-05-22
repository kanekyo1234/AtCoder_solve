import math

n=int(input())
e = [[int(i) for i in input().split()] for i in range(n)] 
c=0

for i in range(n):
    for j in range(n):
        if i!=j:
            c+=math.sqrt((e[i][0]-e[j][0])**2+(e[i][1]-e[j][1])**2)
print(c/n)

