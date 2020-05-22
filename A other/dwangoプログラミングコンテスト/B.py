s=str(input())
n=len(s)
#print(s.count('25'))
jugh=0
jump=1
i=0
count1=0
ans=0
while i<=n-2:
    if s[i:i+2]=="25":
        if jugh==0:
            jugh=1
            count1+=1
            ans+=count1
        else:
            count1+=1
            ans+=count1
        i+=2
    else:
        if jugh==1:
            jugh=0
            count1=0
        i+=1

print(ans)


"""
ans.append(count)
if ans[0]==0:
    print(0)
    exit()
ansa=0
for i in range(len(ans)):
    counta=1
    for j in range(2,len(ans[i])//2+1):
        counta+=j
    ansa+=counta
print(ansa)

"""

