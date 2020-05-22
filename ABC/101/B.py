n=int(input())
a=str(n)
a=list(a)
count=0
for i in range(len(a)):
    count+=int(a[i])

if n% count ==0:
    print("Yes")
else:
    print("No")