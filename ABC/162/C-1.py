import math
from itertools import  product

k=int(input())
k+=1

for z in product((k), repeat=k):
    print(z)
