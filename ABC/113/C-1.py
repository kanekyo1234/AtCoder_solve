
n,m=map(int,input().split())
py=[]
for i in range(m):
    py.append([i]+list(map(int,input().split())))

py.sort(key=lambda na:(na[1],na[2]))
print(py)
count=0
m_city=py[0][1]
for i in range(m):
    si=py[i][1]
    if m_city==si:
        count+=1
        py[i].append(count)
    else:
        count=1
        m_city=py[i][1]
        py[i].append(count)
    
py.sort(key=lambda na:na[0])


for i in range(m):
    print('{:0>6}'.format(py[i][1]),end="")
    print('{:0>6}'.format(py[i][3]))
    
     