import fractions
n,m=map(int,input().split())
s=list(str(input()))
t=list(str(input()))

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

l=lcm(n, m)
index=fractions.gcd(n,m)
#print(indexn,indexm)
for i in range(index):
    #print(i)
    if s[n//index*i]!=t[m//index*i]:
        print(-1)
        break
else:
    print(l)

"""

for i in range(n):
    index=l//n*i+1
    print(index)

    if ans[index]==0:
        ans[index]=s[i]
print(ans)
for i in range(m):
    index=l//m*i+1
    print(t[i])
    print(index)
    if ans[index]==0:
        ans[index]=t[i]
    else:
        if t[i]!=ans[index]:
            print(-1)
            exit()
print(ans)
print(l)
"""
