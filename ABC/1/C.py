
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
n,w=map(int,input().split())
ans=['NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
n=n//10+(n%10/10)
#print(n)
if w < 0.25 * 60:
    W = 0
elif 0.25 * 60 <= w < 1.55 * 60:
    W = 1
elif 1.55 * 60 <= w < 3.35 * 60:
    W = 2
elif 3.35 * 60 <= w < 5.45 * 60:
    W = 3
elif 5.45 * 60 <= w < 7.95 * 60:
    W = 4
elif 7.95 * 60 <= w < 10.75 * 60:
    W = 5
elif 10.75 * 60 <= w < 13.85 * 60:
    W = 6
elif 13.85 * 60 <= w < 17.15 * 60:
    W = 7
elif 17.15 * 60 <= w < 20.75 * 60:
    W = 8
elif 20.75 * 60 <= w < 24.45 * 60:
    W = 9
elif 24.45 * 60 <= w < 28.45 * 60:
    W = 10
elif 28.45 * 60 <= w < 32.65 * 60:
    W = 11
elif 32.65 * 60 <= w:
    W = 12
 
if W == 0:
    print("C",0)
    exit()
 

for i in range(0,len(ans)):
    if 11.25+22.5*i<=n and n<=11.25+22.5*(i+1):
        print(ans[i],W)
        break
else:
    print("N",w)
