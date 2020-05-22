s=str(input())
n=len(s)
a=[0]
count=0
for i in range(n):
    if s[i:i+1]=='<':
        count+=1
        a.append(count)
    else:
        count=0
        a.append(0)
#print(a)
count=0
for i in range(n-1,-1,-1):
    if s[i:i+1]=='>':
        count+=1
        a[i]=max(a[i],count)
    else:
        count=0

print(sum(a))