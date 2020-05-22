n=int(input())
s=[str(input()) for _ in range(n)]
ans=0

a=list(set(s))
for asa in a:
    count=0
    for i in range(n):
        if s[i]==asa:
            count+=1
    if ans<count:
        ans=count
        sa=asa
print(sa)