s=str(input())
n=len(s)
matome=[]
i=0
while i<n:
    now=s[i:i+1]
    j=1
    i+=1

    while s[i:i+1]==now:
        i+=1
        j+=1
    matome.append(j)
#print(matome)
s=list(s)
count=0
ans=[]
i=0
while i<n:
    if s[i]=="R" and s[i+1]=="L":
        sum_m = matome[count]+matome[count+1]
        if sum_m%2==0:
            ans.append(sum_m//2)
            ans.append(sum_m//2)
        else:
            if matome[count]%2==1:
                ans.append(sum_m//2+1)
                ans.append(sum_m//2)
            else:
                
                ans.append(sum_m//2)
                ans.append(sum_m//2+1)
        count+=2
        i+=2
    else:
        ans.append(0)
        i+=1
    
for i in range(n):
    print(ans[i],end=" ")


