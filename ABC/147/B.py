a=list(str(input()))
b=len(a)-1
count=0
for i in range(len(a)//2):
    if a[i]!=a[b]:
        count+=1
    b-=1
print(count)