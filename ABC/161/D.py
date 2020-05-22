n=int(input())
suma=[[2,3,3,3,3,3,3,3,3,2]]
ans=""
if n<=9:
    print(n)
else:
    n-=9

for i in range(11):
    b=[suma[i][0]+suma[i][1]]
    for j in range(1,9):
        b.append(suma[i][j-1]+suma[i][j]+suma[i][j+1])
        
    b.append(suma[i][-2]+suma[i][-1])
    suma.append(b) 
for i in range(11):   
    print(suma[i])
count=0
for i in range(11):
    for j in range(1,10):
        if n<=suma[i][j]:
            atai=i+2
            keta=j
            count=1
            break
        else:
            n-=suma[i][j]
    print(n)
    if count==1:
        print(n)
        break
    #print(n)

print(atai,keta)
ans+=str(keta)
print(n,"n")
for z in range(atai-1):
    count=0
    for i in range(11):
        for j in range(1,10):
            if n<=suma[i][j]:
                atai=i+2
                keta=j+
                count=1
                break
            else:
                n-=suma[i][j]
        if count==1:
            break
    print(n)
    ans+=str(keta)    
print(ans)

