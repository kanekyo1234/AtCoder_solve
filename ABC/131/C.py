
import fractions
a,b,c,d=map(int,input().split())
x1=b//c-(a-1)//c #ｃの割れるやつ
x2=b//d-(a-1)//d #ｄの割れるやつ
sks=c * d // fractions.gcd(c,d)#最小公倍数　普通ならmathメソッドにある
x3=b//sks-(a-1)//sks#ｃ＊ｄの割れるやつ
ans=b-a+1-(x1+x2-x3)
print (ans)
