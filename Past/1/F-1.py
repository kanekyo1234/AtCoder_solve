s=str(input())
start=0
jugh=0
ans=[]
for i in range(0,len(s)):
   # print(ord(s[i:i+1]),s[i:i+1])
    if ord(s[i:i+1])<97:#大文字
        if jugh==0:
            jugh=1
            start=i
        else:
            jugh=0
            ans.append(list(s[start:i+1]))
#print(ans)
for i in range(len(ans)):    
    ans[i][0]=chr(ord(ans[i][0])+32)
    ans[i][-1]=chr(ord(ans[i][-1])+32)
ans.sort()
for i in range(len(ans)):    
    ans[i][0]=chr(ord(ans[i][0])-32)
    ans[i][-1]=chr(ord(ans[i][-1])-32)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end="")
print()