import math
w,h=map(int,input().split())
count=1
count2=1
count=math.factorial(h-1)
count1=math.factorial(w-1)
count*=count1
count2*=math.factorial(w+h-2)

mod=10**9+7
print((count2//count)%mod)


