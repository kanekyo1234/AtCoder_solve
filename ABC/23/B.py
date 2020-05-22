n=int(input())
s=list(str(input()))
if n%2==0:
    print(-1)
    exit()
if s[n//2]!='b':
    print(-1)
    exit()
j=-1
a=['a','c','b']
b=['c','a','b']

for i in range(1,n//2):
    if s[n//2+i]!=b[(i-1)%3] or s[n//2+j]!=a[(abs(j)-1)%3]:
        print(-1)
        break
    j-=1
else:
    print(n//2)