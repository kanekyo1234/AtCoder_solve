n,d,k=map(int,input().split())

l=[]
r=[]
for i in range(d):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)

s=[]
t=[]

for i in range(k):
    c,e=map(int,input().split())
    s.append(c)
    t.append(e)


for i in range(k):
    count=0
    start=s[i]
    goal=t[i]
    #print(start,goal)
    if start<goal:
        for j in range(d):
            #print(j,"dfg")
            if l[j]<=start:
                if goal<=r[j]:
                    count=j+1
                    #print("DFGHJ")
                    break
                else: 
                    if start<=r[j]:
                        start=r[j]
                    
    else:
        #print(" start>goal")

        for j in range(d):
           # print(start,goal)
            if start<=r[j] :
                if goal>=l[j]:  
                    count=j+1
                    break
                else:
                    if start>=l[j]:
                        start=l[j]
    print(count)
