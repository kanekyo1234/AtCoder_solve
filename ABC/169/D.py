import collections
n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


ans = 0
# print(prime_factorize(n))
a = collections.Counter(prime_factorize(n))
for v in a.values():
    ans += (v+1)//2

print(ans)
