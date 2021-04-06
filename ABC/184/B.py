n, x = map(int, input().split())
s = input()

for i in s:
    if i == "x":
        x = max(x-1, 0)
    else:
        x += 1
print(x)
