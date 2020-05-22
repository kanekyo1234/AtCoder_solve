n,m=map(int,input().split())
a=30*(n%12)+m/2
b=6*m
#print(a,b)
if 180<abs(a-b):
    print(360-abs(a-b))
    exit()
print(abs(a-b))
