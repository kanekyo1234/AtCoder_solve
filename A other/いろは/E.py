n,a,b=map(int,input().split())
if b==0:
    print(n-n//a)
    exit()
d=list(map(int,input().split()))
d.sort()
ans=n-b
d.insert(0,0)
count=0#dと過分内で消すやつ
for i in range(len(d)-1):

    if a<=d[i+1]-d[i]:
        if d[i]+a not in d:
            count+=(d[i+1]-d[i]-1)//a
            #print(count,i,"SDF")
#print(count)
if n-d[-1]%a!=0 and a<=n-d[-1]:
    count+= (n-d[-1])//a
#print(count)

#print(ans,count)
print(ans-count)

kaburi=0





"""
count=0
for i in range(b):

count2=0
d.insert(0,0)
d.append(n)
for i in range(b+1):
    count2+=(d[i+1]-d[i])//a

print(n,count2,b,count)
print(n-count2-b+count)"""