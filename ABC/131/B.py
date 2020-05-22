a,b=map(int,input().split())
sum1=0
min1=1000

for i in range(a):
    if abs(min1)>abs(b):
        min1=b
    sum1+=b
    b+=1

print(sum1-min1)
