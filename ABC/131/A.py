n=list(map(int,input()))
count=0
for i in (range(3)):
    if n[i]==n[i+1]:
        count+=1
if count>=1:
    print("Bad")
else:
    print("Good")