n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]



sort_ab = sorted(ab, key=lambda x:(x[1], x[0]))
#print(sort_ab)
count=0
for i in range(n):
    count+=sort_ab[i][0]
    if sort_ab[i][1]<count:
        print("No")
        break
else:
    print("Yes")