a=int(input())
keta=0
for i in range(1,12):
    if a<=26**i:
        keta=i
        break
    
#print(keta)

ans=""

for j in range(keta-1,-1,-1):
    #print(j,"j")
    hiku=26**j
    for i in range(1,27):
       # print(hiku*i)
        if a<=hiku*i:
           # print(a,i,"a")
            
            if a==hiku*i:
                a-=hiku*(i-1)

                ans+=chr(i+97-1)
            else:
                a-=hiku*(i-1)
                ans+=chr(i+96-1)
            break
print(ans)
"""
        hiku*i
    print(a%(26**i))
    a-=a%(26**i)
    print(a)
"""