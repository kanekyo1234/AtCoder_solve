n,k,m,r=map(int,input().split())
s=[int(input()) for _ in range(n-1)]
ave=0
s.sort(reverse=True)

if n==k:
    print(max(sum(s)-r*k,0))
    exit()

for i in range(k):
    ave+=s[i]

#print(ave)

if ave-s[k-1]+m<r*k:
    print(-1)
else:
    if r*k<=ave:
        print(0)
    else:
        print(r*k-(ave-s[k-1]))
