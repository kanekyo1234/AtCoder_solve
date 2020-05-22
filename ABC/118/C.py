"""
import math
n=int(input())
a=list(map(int,input().split()))
m1=min(a)

def a_gcd(t,y):
    return math.gcd(t,y)

if m1==1:
    print(m1)
    exit()
for i in range(n):
    m1=a_gcd(m1,a[i])
    if m1==1:
        break

print(m1)
"""
import fractions
n=int(input())
a=list(map(int,input().split()))
m1=min(a)

def a_gcd(t,y):
    return  fractions.gcd(t,y)

if m1==1:
    print(m1)
    exit()
for i in range(n):
    m1=a_gcd(m1,a[i])
    if m1==1:
        break

print(m1)