h,w=map(int,input().split())

a=[]
a.append(["#" for i in range(2+w)])
for i in range(h):
    a.append(["#"]+list(input())+["#"])
a.append(["#" for i in range(2+w)])

for i in range(h+2):
    for j in range(w+2):
        print(a[i][j],end="")
    print()