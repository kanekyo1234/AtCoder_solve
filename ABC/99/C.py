n=int(input())
#print(9**5)
ans=0


ans=0
while 5<n:
    if n%9==0:
        for i in range(1,17):#９
            if n<9**i:
                if 9<=n:
                    n-=9**(i-1)
                    ans+=1
                    print(ans,n,9,i,9**(i-1))
                break

        for i in range(1,17):
            if n<6**i:
                if 6<=n:
                    n-=6**(i-1)
                    ans+=1
                print(ans,n,6,i,6**(i-1))
                break    
    else:
        for i in range(1,17):
            if n<6**i:
                if 6<=n:
                    n-=6**(i-1)
                    ans+=1
                print(ans,n,6,i,6**(i-1))
                break
        
        for i in range(1,17):#９
            if n<9**i:
                if 9<=n:
                    n-=9**(i-1)
                    ans+=1
                    print(ans,n,9,i,9**(i-1))
                break
    
print(ans+n)