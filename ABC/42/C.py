import functools

n,k=map(int,input().split())
d=list(map(int,input().split()))

for i in range(n,n*11):
    count=0
    l = [int(x) for x in list(str(i))]
    for j in l:
        #print(j)
        
        if j  not in d :
            count+=1
    if count==len(l):
        print( int(functools.reduce(lambda x, y: x + y, [str(x) for x in l])))
        exit()
