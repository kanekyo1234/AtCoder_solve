n=int(input())
def search(k,m):
    count=0
    while 0<k:
        count+=k%m
        k=k//m
    return count
ans=10**6
for i in range(n+1):
    
    ans=min(ans,search(i,9)+search(n-i,6))
    #print(search(i,6),search(n-i,9))
    #print(ans)
print(ans)
