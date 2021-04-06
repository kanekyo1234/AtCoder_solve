n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ok=0 #大丈夫なとこまで
ab=sorted(ab, key=lambda x:(x[0], -x[1]))
print(ab)
count=[]
ans=[0]
for i in range(n):
    for j in range(1,i+1):
       # print(ab[ok][0],ok)
        if ok<n-1 and ab[ok][0]<=j:
            print(ab[ok][1])
            ans.append(ab[ok][1])
            print(ans,"ERTY")
            ok+=1 
        else:
            break
    ans=ans.sort(reverse=True)
    print(ans,"DFGH")
    count.append(ans.pop(0))
a=0
for i in range(n):
    a+=count[i]
    print(a)

