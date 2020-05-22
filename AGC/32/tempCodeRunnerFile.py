n=int(input())
b=list(map(int,input().split()))
ba=[]#右からの距離を足したやつ
for i in range(n):
    ba.append(b[i]+n-1-i)
print(ba)
ans=[0]*n
#for i in range(n):

    