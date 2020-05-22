n=int(input())
a=sorted(list(map(int,input().split())))

b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))
#print(a)
#print(b)
#print(c)
c_count=[]#cから行けるところの回数
b_count=[]#bから行けるところの回数

j=0
count=0
for i in range(n):#cから行けるところの回数
    for j in range(count,n):
        
        if b[j]<c[i]:
 #           print("dfghj")
            count+=1
        else:
  #          print("GHJK")
            break
    c_count.append(count)

count=0

for i in range(n):#bから行けるところの回数
    for j in range(count,n):
        if a[j]<b[i]:
            count+=1
        else:
            break
    b_count.append(count)

ans=0
#print(b_count)
#print(c_count)

#ここ累積和にしないとTLEしちゃう　sumにしてたら間に合わなかった

for i in range(1,n):
    b_count[i]+=b_count[i-1]
#print(b_count)



for i in range(n):
    if 0<=c_count[i]-1:
        ans+=b_count[c_count[i]-1]

print(ans)

#print(b_count)
#print(c_count)
