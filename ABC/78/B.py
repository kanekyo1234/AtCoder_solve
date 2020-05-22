x,y,z=map(int,input().split())
x-=z
c=0
while y<=x:
    x-=y
    x-=z
    c+=1
print(c-1)
