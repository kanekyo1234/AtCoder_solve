s=int(input())
count=0
for i in range(len(str(s))):
    if s%10==1:
        count+=1
    s=s//10
print(count)