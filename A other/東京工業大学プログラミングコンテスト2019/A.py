a, b, t = map(int, input().split())

c = b-a
while a < t:
    a += c
print(a)
