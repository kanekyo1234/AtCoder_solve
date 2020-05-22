import itertools
a = int(input())
ans1=0
ans2=0
b=[]
for i in range(1,a+1):
    b.append(str(i))

p=list(map(str,input().split()))
q=list(map(str,input().split()))
count=0
for v in itertools.permutations(b):
    if list(v)==p:
        ans1=count+1
    if list(v)==q:
        ans2=count+1
    count+=1
print(abs(ans1-ans2))