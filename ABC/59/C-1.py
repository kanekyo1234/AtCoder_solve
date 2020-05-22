n=int(input())
a=list(map(int,input().split())) 
rui=[0]*n
#奇数がマイナス時
kisuu=[]
guusuu=[]
count1=0
count2=0

for i in range(n):
    if i%2==0:
        if a[i]<0:
            kisuu.append(a[i]+abs(a[i]))
            count1+=a[i]
        else:
            kisuu.append(a[i])
    else:
        if 0<=a[i]:
            kisuu.append(a[i]-abs(a[i]))
            count1+=a[i]
        else:
            kisuu.append(a[i])



#偶数がマイナス時
for i in range(n):
    if i%2!=0:
        if a[i]<0:
            guusuu.append(a[i]+abs(a[i]))
            count2+=a[i]
        else:
            guusuu.append(a[i])

    else:
        if 0<=a[i]:
            guusuu.append(a[i]-abs(a[i]))
            count2+=a[i]
        else:
            guusuu.append(a[i])

print(kisuu)
print(guusuu)
print(count1,count2)