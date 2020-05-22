n=int(input())
w=[]
for i in range(n):
    w.append(int(input()))

noseru=0#帰れるか帰れないか
ans=[]
ans.append(w[0])
soezi=0#変えるやつ
mina=10**7#差が小さいやつ
for i in range(1,n):
    for j in range(len(ans)):
        if ans[j]>=w[i]:
            ans[j]=w[i]
            noseru+=1
            break
    if noseru==0:
        ans.append(w[i])
    noseru=0
    #print(ans)
    ans.sort()
print(len(ans))