x=int(input())
a=100
for i in range(0,5000):
    if int(a*1.01)>=x:
        print(i+1)
        break
    else:
        a=int(a*1.01)