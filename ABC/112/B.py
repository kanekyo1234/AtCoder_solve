n,t=map(int,input().split())
ct=[list(map(int,input().split())) for _ in range(n)]


ct=sorted(ct, key=lambda x:(x[0], x[1]))

for i in range(n):
    if ct[i][1]<=t:
        print(ct[i][0])
        break
else:
    print("TLE")