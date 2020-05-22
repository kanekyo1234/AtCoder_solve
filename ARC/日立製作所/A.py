s=list(str(input()))
if len(s)%2==1:
    print("No")
else:
    for i in range(0,len(s),2):
        if s[i]!='h' or s[i+1]!='i':
            print("No")
            break
    else:
        print("Yes")
        
    
