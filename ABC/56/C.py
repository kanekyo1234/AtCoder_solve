n=int(input())
a=[1]
i=0
count=2
while(a[i]<n):
    a.append(a[i]+count)
    count+=1
    i+=1
#print(a)
print(count-1)