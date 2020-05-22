
n=int(input())
s=str(input())
e_cnt=s.count('E')
num=[0]*n #Wの数
num2=[0]*(n+1) #Eno左から数えた数
count=0
count2=0
for i in range(n):
    if s[i]=='W':
        num[i]=count
        num2[i]=e_cnt-count2
        count+=1
    else:
        num[i]=count
        num2[i]=e_cnt-count2 
        count2+=1
    
   
print(num,num2)

ans=[0]*n#リーダーを決めるとき

for i in range(n):
    ans[i]=abs(num[i]+num2[i+1])
print(min(ans))

