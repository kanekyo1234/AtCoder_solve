import collections
n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(b[i-1]+a[i])
# print(b)
ans = b.count(0)
d = collections.Counter(b)
for i in d.values():
    ans += i*(i-1)//2  # iC2 組み合わせ

print(ans)
