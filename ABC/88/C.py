c=[]
for i in range(3):
    c.append(list(map(int,input().split())))

for i in range(2):
    if c[0][i]-c[0][i+1]!=c[1][i]-c[1][i+1] or  c[1][i]-c[1][i+1]!=c[2][i]-c[2][i+1]:
        print("No")
        exit()
print("Yes")