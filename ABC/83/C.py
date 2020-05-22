import math
x,y=map(int,input().split())

def ans(x,x2,y):
    if x>y:
        return 0
    else:
        return ans(x2,x2*2,y)+1

print(ans(x,x*2,y))