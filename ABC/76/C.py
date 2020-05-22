s=str(input())
t=str(input())
s=list(s)
t=list(t)
count2=0
count=0

#辞書順なので後ろから数えることによって
"""
??????
wer
weraaa
がこうなる
??????
wer
aaawer

forを逆にしなければならない
"""

for i in range(len(s)-len(t),-1,-1):
    for j in range(len(t)):
        #print(s[i+j])
        if s[i+j]!='?' and  s[i+j]!=t[j]:
            count=0
            break
        else:
            count+=1
        #print(count)
    
    if count==len(t):
        for z in range(len(s)):
            if z<i or i+len(t)-1<z:
                if s[z]=='?':
                    print("a",end="")
                else:
                    print(s[z],end="")
            else:
                #print(count2)
                print(t[count2],end="")
                count2+=1
        exit()
    count=0
print("UNRESTORABLE")
