s=list(map(str,input().split()))
n=int(input())
t=[str(input()) for _ in range(n)]


for i in range(len(s)):
    if s[i] in t:
        for i in range(len(s[i])):
            print("*",end="")
        print(" ",end="")

    else:
        for j in range(n):
            if "*" in t[j]:
                count=0
                for f in range(len(t[j])):
                    #print(count)
                    if t[j][f:f+1]!="*":
                        count+=1
                
                if 1<=count:

                    if len(t[j])==len(s[i]):
                        for z in range(len(s[i])):
                            if s[i][z:z+1]==t[j][z:z+1]:
                                for i in range(len(s[i])):
                                    print("*",end="")
                                print(" ",end="")  
                                break   
                    else:
                        print(s[i],end=" ")
                        break

                else:
                    if len(t[j])==len(s[i]):
                        for i in range(len(s[i])):
                            print("*",end="")
                        print(" ",end="")
                        break
                    else:
                        print(s[i],end=" ")
                        break
        else:
            print(s[i],end=" ")
                
                   
            
            
                    


print()