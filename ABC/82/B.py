s=list(str(input()))
t=list(str(input()))
s.sort()

t.sort(reverse=True)
#print(s,t)

for i in range(min(len(s),len(t))):
   # print(s[i],t[i])
    if s[i]<t[i]:
        print("Yes")
        exit()
    elif s[i]>t[i]:
        print("No")
        exit()
if len(s)<len(t):
    print("Yes")
else:
    print("No")