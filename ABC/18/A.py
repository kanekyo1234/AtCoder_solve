a = int(input())
b = int(input())
c = int(input())

d = [a, b, c]
d.sort()
print(3-d.index(a))
print(3-d.index(b))
print(3-d.index(c))
