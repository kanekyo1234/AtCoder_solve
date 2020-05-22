n=int(input())
s=str(input())
s=list(s)
ans=0
count=0
for i in range(n):
    if s[i]=="I":
        count+=1
    else:
        count-=1
    if ans<count:
        ans=count
print(ans)