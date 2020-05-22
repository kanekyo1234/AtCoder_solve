s=str(input())
k=int(input())
a=list(s)
print(a)
sub=set()
for i in range(len(a)):
    sub.add(a[i])
sub=sorted(sub)
print(sub)

start=sub[0]
nexts=""
count=2 #文字列の長さ
for i in range(len(a)-count):
    if a[i]==start:
        for j in range(count):
            nexts+=a[i+j]
        print(nexts)
        sub.append(nexts)
        print(sub)


