s=str(input())
t=str(input())

for i in range(len(s)):
    if s==t:        
        print("Yes")
        exit()
    else:
        s=s[-1]+s[:-1]
    #print(s)
print("No")
