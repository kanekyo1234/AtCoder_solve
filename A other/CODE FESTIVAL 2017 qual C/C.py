"""
import collections
s=list(str(input()))

s=collections.Counter(s)
print(s)
x=s['x']
print(x)
count=0
kisuu=[]
for ss,v in s.items():
    
    if v%2!=0:
        kisuu.append(ss)
        count+=1

print(kisuu)
print(count)
if 'x' in kisuu:
    count-=1
print(count)
if count<=1:
    print()
    """

b=str(input())
x=0
x=b.count('x')
#print(a)
a=list(b.split('x'))
#print(x)
s=""
for i in range(len(a)):
    s+=a[i]
#print(s)

mannnaka=0
mannnaka2=0

if len(s)==0:
    print(0)
        
    exit()
if len(s)==1:
    #print(x)
    for i in range(len(b)):
        if b[i]==s:
            mannnaka=i
            break
    print(abs(b[0:mannnaka].count('x')-b[mannnaka:len(b)].count('x')))
    exit()
if len(s)%2==1:
    asd=s[len(s)//2+1:len(s)]
    #print(asd)
    asd=asd[::-1]
   # print(s[0:len(s)//2],asd)
    if s[0:len(s)//2]==asd:
        saa=s[len(s)//2]
        for i in range(len(b)):
            if b[i]==saa:
                mannnaka=i
                break
        print(abs(b[0:mannnaka].count('x')-b[mannnaka:len(b)].count('x')))
        
    else:
        print(-1)
else:
    asd=s[len(s)//2:len(s)]
    asd=asd[::-1]
   # print(s[0:len(s)//2],asd)

    if s[0:len(s)//2]==asd:
        saa=s[len(s)//2]
        for i in range(len(b)):
            if b[i]==saa:
                mannnaka=i
                break
        print(abs(b[0:mannnaka].count('x')-b[mannnaka+1:len(b)].count('x')))
        
        
        
        #print(x)
    else:
        print(-1)

    

