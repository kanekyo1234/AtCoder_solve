a=str(input())

plus=a.split('+')
#print(plus)
ans=0
for i in range(len(plus)):
    if plus[i].count('0')==0:
        ans+=1
print(ans)