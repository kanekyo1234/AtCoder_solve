a, b, c = map(int, input().split())
a = abs(a)
if b*c <= a:
    print(a-b*c)
else:
    kaisuu = a//c
    saisyo = a % c
    print(kaisuu, saisyo)
    b = b-kaisuu
    if b % 2 == 1:
        print(abs(c-saisyo))
    else:
        print(abs(saisyo))
