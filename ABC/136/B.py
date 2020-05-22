n=int(input())
count=0
for i in range(1,n+1):
    num = len(str(i))
    if num%2==1:
        count+=1
print(count)
