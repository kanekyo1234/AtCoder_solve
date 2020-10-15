n = int(input())
ans = 0
for i in range(1, n+1):
    for i in range(n):

    y = (n//i)
    ans += (1+y)*y*i/2
print(int(ans))
