#二回目
import math
a,b,c,d=map(int,input().split())
def lcm(x, y):
    return (x * y) // math.gcd(x, y)


ans1=b
a-=1
ans2=0
ans1-=b//c
ans1-=b//d

ans1+=b//(lcm(c,d))
#print(ans1)

ans2+=a//c
ans2+=a//d
ans2-=a//(lcm(c,d))
print(ans1-(a-ans2))