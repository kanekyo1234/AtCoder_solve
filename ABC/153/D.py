h=int(input())
count=0
t=1
while(h!=0):
    h=h//2
    count+=t
    t*=2
print(count)