n=int(input())
w=[str(input()) for _ in range(n)]

if len(set(w))!=n:
    print("No")
    exit()

for i in range(n-1):
    if w[i][-1]!=w[i+1][0]:
        print("No")
        break
else:
    print("Yes")