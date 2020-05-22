a,b,x=map(int,input().split())


L=0
R=10**9+1

def ans(center):
    return a*center + b*len(str(center))

while R-(L+1)>0:
    center=(R+L)//2
    count=ans(center)
    if x>=count:
        L=center
    else:
        R=center
print(L)