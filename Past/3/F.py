n=int(input())
s=[list(str(input())) for _ in range(n)]
ans=""
for i in range(n//2):
    s2=set(s[i])
    for j in s2:
        if j in s[n-i-1]:
            ans+=j
            break
    else:
        print(-1)
        exit()
    
print(ans,end="")
if n%2==1:
    print(s[n//2][0],end="")
print(ans[::-1],end="")
