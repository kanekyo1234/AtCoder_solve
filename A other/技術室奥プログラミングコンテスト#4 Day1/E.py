n,m,k,e=map(int,input().split())
a=list(map(int,input().split()))
bc=list(map(int,input().split()))
b=[]
bc.sort(reverse=True)
for i in range(k):
    b.append(bc[i])
sume=e+sum(b)

suma=sum(a)

#print(suma,sume)
if suma<=sume:
    ans=k
    b.sort()
    #print(b)
    for i in range(m):
     #   print(suma,sume-b[i],ans)
        if suma<=(sume-b[i]):
            sume-=b[i]
            ans-=1
      #      print(ans)
        else:
            break
    print("Yes")
    print(ans)

else:
    ans=0
    a.sort()
    for i in range(n):
        if sume>=a[i]:
            ans+=1
            sume-=a[i]
    print("No")
    print(ans)

#for i in range()