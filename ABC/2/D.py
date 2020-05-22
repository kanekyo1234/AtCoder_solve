from itertools import  product

n,m=map(int,input().split())

#1から交流ある谷内を抜き出しそれぞれ見ていく
s=[]

for i in range(m):
    s.append(list(map(int,input().split())))
ans=1

adlist=[ [i+1] for i in range(n)]#交流のあるやつ同士の隣接リスト
for i in range(m):#1から順に見ていく
    x=s[i][0]
    y=s[i][1]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
#print(adlist)

for z in product((0, 1), repeat=n):
    index_1=[]
    for i in range(n):
        if z[i]==1:
            index_1.append(i+1)
    
    c_okiba=[]#01101とかのインデントの数字をカウントした八のおきば
    #print(index_1)    
    for i in range(n):  
        c=0
        for j in range(len(index_1)):
            #print(index_1[j],adlist[i])
            
            if index_1[j] in adlist[i]:
                c+=1
            
        c_okiba.append(c)
    #print(c_okiba)
    #print(c_okiba.count(len(index_1)),len(index_1))
    if c_okiba.count(len(index_1))==len(index_1):#123 234だったりするときは２３が入っているのでそれの和人index_iの長さが同じならよい
        ans=max(ans,len(index_1))

#print(index_1)
print(ans)



    
"""
adlist=[ [i+1] for i in range(n)]#交流のあるやつ同士の隣接リスト
for i in range(m):#1から順に見ていく
    x=s[i][0]
    y=s[i][1]
    adlist[x-1].append(y)
    adlist[y-1].append(x)
print(adlist)


for i in range(1,n+1):#1から順に見ていく
    i_list=[]
    for j in range(m):
        x=s[j][0]
        y=s[j][1]
        if x==i:"""