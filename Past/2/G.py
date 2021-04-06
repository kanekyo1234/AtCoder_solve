
q=int(input())

qq=[list(map(str,input().split())) for _ in range(q)]
ans=""
index=0
atai=[]
len_ans=0
for i in range(q):
    if int(qq[i][0])==1:
        ans+=qq[i][1]+qq[i][2]
        atai.append(int(qq[i][2]))
        len_ans+=int(qq[i][2])
        print(ans)
    else:
        count=0
        if int(qq[i][1])<=len_ans:
            x=int(qq[i][1])
            sub_count=0#引いた回数
           
            for j in range(index,len(atai)):
                if atai[j]<x:
                    x-=atai[j]
                    index+=1
                    count+=atai[j]**2    
                    sub_count+=1
                    len_ans-=  atai[j]
                else:
                    count+=x**2
                    atai[j]-=x
                    len_ans-=x
                    
                    break
                
            print(count)
            ans=ans[sub_count*2:len(ans)+1]
            ans=list(ans)
            if len(ans)!=0:
                ans[1]=str(atai[j])
            ans="".join(ans)
        else:
            for j in range(index,len(atai)):
                count+=atai[j]**2
                index+=1
            print(count)
            ans=""
#print(ans)


