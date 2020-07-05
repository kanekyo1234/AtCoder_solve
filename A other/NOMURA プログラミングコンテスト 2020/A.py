h,m,h2,m2,k=map(int,input().split())
a=h*60+m
b=h2*60+m2
if a>b:
    b+=60*24
#print(b)

print(((b-a)-k))