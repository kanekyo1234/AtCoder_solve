k,t=map(int,input().split())

a=list(map(int,input().split()))

print(max(max(a)-1-(k-max(a)),0))