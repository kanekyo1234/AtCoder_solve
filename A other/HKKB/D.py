t = int(input())
mod = 1000000007
for i in range(t):
    n, a, b = map(int, input().split())
    ac = (n-a+1)**2
    bc = (n-b+1)**2
    zenbu = ac*bc
    dame = (max(a, b)-min(a, b)+1)**2

    print(ac, bc, zenbu, dame)
    print((zenbu-dame*min(ac, bc)) % mod)
