n = int(input())
h = list(map(int, input().split()))
min_count = 10**9+1
max_count = 0
for i in range(n):
    max_count = max(max_count, h[i])
    if max_count-2 >= h[i]:
        print("No")
        break
else:
    print("Yes")
