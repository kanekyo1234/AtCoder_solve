import collections
n=int(input())
w=[]
for i in range(n):
    w.append(str(input()))

w_count=collections.Counter(w)
if max(w_count.values())>=2:
    print("No")
    exit()

for i in range(n-1):
    if w[i][-1]!=w[i+1][0]:
        print("No")
        exit()
print("Yes")
    