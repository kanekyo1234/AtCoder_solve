from collections import deque
s=str(input())
c=0
n=1
q=int(input())
for i in range(q):
    a=input().strip()
    a=list(a)
    #print(a)
    if int(a[0])==1:
        #print("DFGHJ")
        c=+1
        n+=1
    if c%2==1:
        if int(a[0])==2:
            #print(a[2])
            s=list(s)
            if int(a[2])==2:
                s=deque(s)
                #print(s)
                s.appendleft(str(a[4]))
                #print(s)
                s=list(s)
                #print("DFGH",s)
            else:
                s.append(str(a[4]))
            s=''.join(s)
            #print(s)  
            for i in range(n%2):
                s=s[::-1]
            n=0
    else:    
        if int(a[0])==2:
        #print(a[2])
            s=list(s)
            if int(a[2])==1:
                s=deque(s)
                #print(s)
                s.appendleft(str(a[4]))
                #print(s)
                s=list(s)
                #print("DFGH",s)
            else:
                
                s.append(str(a[4]))
            s=''.join(s)
            #print(s) 
            for i in range(n%2):
                s=s[::-1]
            n=0

print(s)
