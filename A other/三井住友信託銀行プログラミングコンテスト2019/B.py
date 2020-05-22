
import math
a=int(input())
if (a/1.08)%1==0:
    print (math.ceil(a/1.08))
else:
    m=math.ceil(a/1.08)
    if a==math.floor(m*1.08):
        print(math.floor(m))
    else:
        print(":(")
