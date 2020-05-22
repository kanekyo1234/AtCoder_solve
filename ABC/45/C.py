s=str(input())
n=len(s)-1#間間なので-1
#print(s,n)
#print(xy)
bit=[]#1が＋入れる0がいれない
ans=0
c=0
count=[]
def bit_search(bit):
    #print("DFGHNM")
    count=[]#分けたやつを補完するやつ
    global ans
    c=0
    if len(bit)==n:#2**n文の組み合わせを調べる加圧10を交互に入れるためのif
        for i in range(n):
            if bit[i]==1:
                #print(int(s[c:i+1]))
                count.append(int(s[c:i+1]))
                c=i+1#ここの＋１大事
        #print(int(s[c:n+1]))
        count.append(int(s[c:n+1]))
        ans+=sum(count)
        #print(ans,sum(count),bit,c)
        return 
    else:
       #再起化することによって最初にbitの配列を作る必要性をなくした
        #print(bit)
        bit_search(bit+[0])
        bit_search(bit+[1])

bit_search(bit)
print(ans)
