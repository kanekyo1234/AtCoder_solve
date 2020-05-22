import copy
a=int(input())
b=int(input())
w=b
d=[0]*3
count=0
c=[int(i) for i in str(b)]
for i in range(a-len(c)):
    c.insert(0,0)
for i in range(0,1000,1):
    for j in range(2,-1,-1):
        d[j]=i%10
        i=i//10#ここまでは「０，０，０」とか
    for x in range(a-2):
        if d[0]==c[x]:
            for y in range(x+1,a-1):
                if d[1]==c[y]:
                    for z in range(y+1,a):
                        if d[2]==c[z]:
                            count+=1
                            break
                    break
            break
print(count)    