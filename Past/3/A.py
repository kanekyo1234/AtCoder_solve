s=str(input())
t=str(input())

count=0
if s==t:
    print("same")
else:
    for i in range(3):
        if abs(ord(s[i])-ord(t[i]))==32 or s[i]==t[i]:
            count+=1
    if count==3:
        print("case-insensitive")
    else:
        print("different")