s=str(input())
ans=""
count=0
for i in range(len(s)-1,-1,-1):
    if s[i]=="B":
        count+=1
    else:
        if count!=0:
            count-=1
        else :
            ans+=s[i]
print(ans[::-1])