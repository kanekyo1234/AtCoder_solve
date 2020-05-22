a=int(input())
count=0
b=list(map(int,input().split()) )
for i in range(0,len(b),1):
    if i+1!=b[i]:
        count+=1
if count<=2:
    print("YES")
else:
    print("NO")