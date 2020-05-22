a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=0
for i in range(0,a*500+1,500):
    for j in range(0,b*100+1,100):
        for z in range(0,c*50+1,50):
            if i+j+z==x:
                ans+=1
print(ans)
