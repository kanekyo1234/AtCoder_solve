n=int(input())
s=str(input())
a=['A','B','X','Y']
ans=10**10
for a1 in range(4):
    for a2 in range(4):
        for a3 in range(4):
            for a4 in range(4):
                sc=s
                komand1=a[a1]+a[a2]
                komand2=a[a3]+a[a4]
                #print(komand1,komand2)
                if komand1==komand2:
                    continue
                count1=0
                count2=0
                sc=sc.replace(komand1,'R')
                sc=sc.replace(komand2,'L')
                #print(sc)
                count1=len(sc)
               # print(sc)
                sc=s
                #print(sc,s)
                sc=sc.replace(komand2,'R')
                sc=sc.replace(komand1,'L')
                count2=len(sc)
                ans=min(ans,count1,count2)


print(ans)