s=str(input())
k=int(input())
count=1
ans=0
s2=s+s
ans2=0
#print(s2)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        if 2<=count:
            ans+=count//2
        count=1
if 2<=count:
    ans+=count//2
count=1
for i in range(len(s2)-1):
    if s2[i]==s2[i+1]:
        count+=1
    else:
        if 2<=count:
            ans2+=count//2
        count=1

if 2<=count:
    ans2+=count//2
    #print(count)
#print(ans,ans2)
if s[0]==s[-1]:
    print((ans2-ans)*k)
else:
    print(ans*k)

