n,a,b=map(int,input().split())

s=[ int(input()) for _ in range(n)]
s.sort()
mins=s[0]
maxs=s[-1]
if maxs<=mins:
    print(-1)
    exit()
dif=maxs-mins
#print(mins,maxs)
#print(b/dif)
sums=sum(s)*(b/dif)
print(b/dif,(a*n-sums)/n)