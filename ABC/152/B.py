

b,c=map(int,input().split())
bc=c
cb=b
for i in range(b-1):
    bc=(bc*10+c)
for i in range(c-1):
    cb=(cb*10+b)
print(max(bc,cb))