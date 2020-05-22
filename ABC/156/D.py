n,a,b=map(int,input().split())

mod = 10**9+7
aa=[0]*n
import itertools
s= list(itertools.combinations(range(n), a))
print(len(s))