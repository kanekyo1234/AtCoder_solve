n=int(input())

for i in range(0,10001):
    ans=0
    s=list(str(i))
    for j in range(len(s)):
        ans+=int(s[j])*(i**(len(s)-j-1))
        #print(ans)
    #print(ans)
    if ans==n:
        print(i)
        break
else:
    print(-1)