s=input()#1/8
a= [a  for a in s]
count=1
b=[]
d=[a[0]]
while count<len(a):
    if 'A'<=a[count] and a[count]<='Z':
        d.append(a[count])
    else:
        count+=1
