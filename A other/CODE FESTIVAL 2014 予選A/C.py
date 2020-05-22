a,b=map(int,input().split())
a-=1
ans=b//4-(a)//4

a100=b//100-a//100
a400=b//400-a//400
print(ans-a100+a400)