s=list(map(str,input().split()))
n=int(input())
a=[str(input()) for _ in range(n)]

for i in range(len(s)):
    jugh=False
    for j in range(n):
        #print(s[i],a[j],"DFHj")
        if len(s[i])!=len(a[j]):
            continue

        if s[i]==a[j]:
            jugh=True
        count=0
        for z in range(len(s[i])):
            #print(a[j][z],s[i][z])
            if a[j][z]=='*' or a[j][z]==s[i][z]:
               # print("False")
                count+=1
        #print(count,len(s[i]))
        if count==len(s[i]):
            jugh=True

        if jugh==True:
            #print("break",i)
            break
        #print(jugh)
    #print(jugh,"last")
    if jugh==True:
        s[i]="*" * len(s[i])

for i in range(len(s)):
    print(s[i],end=" ")




