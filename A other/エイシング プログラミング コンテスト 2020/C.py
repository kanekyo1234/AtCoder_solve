
n = int(input())
ans = [0]*10001

for i in range(1, 101):
    for j in range(1, 101):
        for z in range(1, 101):
            aaa = i**2+j**2+z**2+i*j+j*z+z*i
            if aaa <= 10**4:
                ans[aaa] += 1
for i in range(n):
    print(ans[i+1])
