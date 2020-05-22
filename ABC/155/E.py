n=list(map(int,input()))
c=n.count(9)
#print(n)
#print(len(n))
ans=0
for i in range(len(n)-1,-1,-1):
    #print(n[i])
    if n[i]<=5:
        ans+=n[i]
    else:
        if i==0:
            #print("a")
            ans+=1
        ans+=10-n[i]#帰ってくる枚数
        j=1
        while n[i-j]==9 and (i-j)!=0:
            #print("sdfghj")
            n[i-j]=0
            j+=1
        n[i-j]=n[i-j]+1
    #print(n[i],ans)
print(ans-c)
