import math
n=int(input())
lr = [list(map(int,input().split())) for _ in range(n)]
global a
a=[2]

def using_sqrt(limit):
    global a
    for k in range(3, limit+1,2):
        factor = 0
        
        # 2以外の偶数は素数ではないので無視する
        if k % 2 == 0 and k != 2:
            continue
        
        # 繰り返しの上限を対象の平方根にする
        for divisor in range(2, math.floor(math.sqrt(k))+1):
            if k % divisor == 0:
                factor += 1
                
        if factor == 0:
            a.append(k)
using_sqrt(100000)
#print(len(a))
