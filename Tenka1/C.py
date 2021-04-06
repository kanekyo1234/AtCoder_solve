n=int(input())
a=4/n
b=a/3
#print(a/3)
"""
print(a/3)
print(1/3498)
print(1/3498 +1/3498 +1/3498)
"""
#print(3485%4)

if n%4==0:
    for i in range(3):
        print(n//4*3,end= " ")
elif n%4==1:
    d=(n+3)//4
    print(d,d*(d*4-5)/3,0)

elif n%4==3:
    print("sdfgb")
else:
    print(n//2,n,n)
    #print(4/n)
    #print(1/(n//2)+1/n+1/n)

"""
count=1

sumb=0
while sumb<1:
    count+=1
    sumb=b*count
if sumb==1:
    print(count,count,count)
else:
    """