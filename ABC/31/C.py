
#変数名が汚いので注意
n=int(input())
a=list(map(int,input().split()))
ta=-50000#高橋の答え
tans=0#高橋の丸つけるans
for i in range(n):#高橋が丸つけたところ
    aa=-50000
    tc=0#青木の一番スコアが高いときの高橋の答えの記録
    for j in range(n):#青木が〇つけたところ
        t=[]
        tcount=0#ｔの要素の合計
        acount=0#
        if i!=j:
            for z in range(min(i,j),max(i,j)+1):#配列を作る
                t.append(a[z])
            for z in range(len(t)):#足す
                if z%2==0:
                    tcount+=t[z]
                else:
                    acount+=t[z]
            if aa<acount:
                aa=acount
                tc=tcount
    if ta<tc:
        ta=tc
print(ta)                



            




    
