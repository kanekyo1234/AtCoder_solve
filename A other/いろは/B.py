s=list(str(input()))
k=int(input())
k=k%len(s)
for i in range(k,len(s)):
    print(s[i],end="")
for i in range(0,k):
    print(s[i],end="")
print()