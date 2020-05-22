a=str(input())
count=0
ans=0
for i in range(len(a)):
    if a[i]== 'A' or a[i]== 'C' or a[i]== 'G' or a[i]== 'T' :
        count+=1
    else:
        ans=max(ans,count)
        count=0
ans=max(ans,count)  
print(ans)