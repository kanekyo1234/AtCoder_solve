import copy
a=list(input())
b=a.copy()
count1=0
count2=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count1+=1
        if a[i]=="0":
            a[i+1]="1"
        else:
            a[i+1]="0"

for i in range(len(b)-2,-1,-1):
    if b[i]==b[i+1]:
        count2+=1
        if b[i+1]=="0":
            b[i]="1"
        else:
            b[i]="0"
print(min(count1,count2))