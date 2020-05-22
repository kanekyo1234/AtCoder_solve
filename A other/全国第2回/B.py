from collections import Counter
n = int(input())
a = [int(i) for i in input().split()] 
if a[0]!=0 : 
     print (0%998244353)
else:
    if a[0]!=1:
        print (0%998244353)
    else :
        a = Counter(a)
        ans = 1
        for i in range(1,len(a)-1): 
            ans*=a[i]**a[i+1]
        print(ans%998244353)

