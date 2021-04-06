h=int(input())
w=int(input())

n=int(input())
a=max(h,w)
count=1
while a*count<n:
    count+=1

print(min(count,h,w))