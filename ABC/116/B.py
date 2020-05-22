s=int(input())
a=[-12345]*100000
for i in range(100000):
    
    a[i]=s
    if s%2==1:
        s=s*3+1
    else:
        s=s/2

    if s in a:
        print(i+2)
        break