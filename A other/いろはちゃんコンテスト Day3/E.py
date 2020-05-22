n=int(input())
c=[ str(input()) for _ in range(n)]
ans=0
for i in range(n):
    if c[i]=='/':
        start=i
        break
else:
    print(0)
    exit()

count1=0
count2=0

c_count=[]
for i in range(start,n):
    if c[i]=='/':
        if count2!=0:
            c_count.append(count2)
            count2=0
        count1+=1
    else:
        if count1!=0:
            c_count.append(count1)
            count1=0
        count2+=1
c_count.append(max(count1,count2))
#print(c_count)
if len(c_count)<2:
    print(0)
    exit()


#print(c_count)
for i in range(0,len(c_count)-1,2):
    if c_count[i]==c_count[i+1]:
        ans+=1
print(ans)

"""

for i in range(n):
    if c[i]=='/':
        count2=0
        count1+=1
    else:
        count2+=1
        if count1==count2:
            ans+=1
            count1=0
        
        if count1<2:
            ans-=1

print(ans)
"""