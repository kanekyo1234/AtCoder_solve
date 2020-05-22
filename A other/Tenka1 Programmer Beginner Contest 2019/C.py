n=int(input())
c=str(input())
#c=c[::-1]
#print(c)
black=c.count('#')
white=n-black
left=0#左は黒を消す
right=white#右はしろを消す
#print(white,black)
ans=right
for i in range(n):
    if c[i]=='#':
        left+=1
    else:
        right-=1
    
    ans=min(ans,left+right)
print(ans)

"""
c_count=[]
count1=0
count2=0


for i in range(n):
    if c[i]=='.':
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

print(c_count)
ans=0
for i in range(0,len(c_count)-1,2):
    ans+=min(c_count[i],c_count[i+1])
print(ans)

"""