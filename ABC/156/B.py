n,k=map(int,input().split())
c=1
ka=k
while n>=ka:
    ka*=k
    c+=1
    #print(ka)
print(c)