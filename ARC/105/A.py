a, b, c, d = map(int, input().split())
if a+b+c+d-(max(a, b, c, d)+min(a, b, c, d)) == max(a, b, c, d)+min(a, b, c, d):
    print("Yes")
elif max(a, b, c, d) == a+b+c+d-max(a, b, c, d):
    print("Yes")
else:
    print("No")
