s,l,r=map(int,input().split())

if s<l :
    print(l)
elif l<=s and s<=r:
    print(s)
else:
    print(r)