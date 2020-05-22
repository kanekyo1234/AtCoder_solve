n=int(input())
n=n%30
a=[1,2,3,4,5,6]
for i in range(n):
    index=i%5
    box=a[index]
    a[index]=a[index+1]
    a[index+1]=box
for i in range(6):
    print(a[i],end="")
print()


