import collections

s=str(input())
t=str(input())

sa=list(s)
ta=list(t)
asa=collections.Counter(sa)
ata=collections.Counter(ta)

casa=[i[0] for i in asa.items() if i[1] >= 2]

cata=[i[0] for i in ata.items() if i[1] >= 2]
print(casa)
print(cata)
if casa==[] and cata==[]:
    print("Yes")
    exit()
aans=[]
tans=[]
for i in range(len(sa)):
    if sa[i] in casa:
        aans.append(ta[i])
for i in range(len(ta)):
    if ta[i] in cata:
        tans.append(sa[i])        
if len(set(aans))==len(casa) and len(set(tans))==len(cata):
    print("Yes")
else:
    print("No")
