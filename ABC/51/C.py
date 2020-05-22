sx,sy,tx,ty=map(int,input().split())

x=tx-sx
y=ty-sy

for i in range(x):
    print("R",end="")

for i in range(y):
    print("U",end="")


for i in range(x):
    print("L",end="")

for i in range(y):
    print("D",end="")
#iki
print("D",end="")
for i in range(x+1):
    print("R",end="")

for i in range(y+1):
    print("U",end="")
print("L",end="")




print("U",end="")
for i in range(x+1):
    print("L",end="")

for i in range(y+1):
    print("D",end="")
print("R",end="")