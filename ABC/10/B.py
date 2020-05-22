n=int(input())
a=list(map(int,input().split()))
ans=0

for i in range(n):
	if a[i] in [2,4,8]:
		ans+=1
	elif a[i]==6:
		ans+=3
	elif a[i]==5:
		ans+=2
print(ans)