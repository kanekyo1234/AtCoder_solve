import math
a,b,x=map(int,input().split())

"""
平面で考える　
こぼれるときに水が台形になってるなら三角形にする
（直角）三角形の長さを求めてhttps://keisan.casio.jp/exec/system/1259903491　にある計算をする
"""
s=x/a#平面化

if a*b==s:
    print(0)
    exit()

if a*b/2 < s:  #台形
    a1=a
    b1=b-(s/a*2-b)


else: #三角形
    a1= s*2/b 
    b1=b
#print(a1,b1)
ans=math.atan(b1/a1)#サイトの計算
#print(ans)
print(ans*(180.0/math.pi))#ラジアンを角度変換する