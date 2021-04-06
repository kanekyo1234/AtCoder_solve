s,t=map(str,input().split())

if s[1]=='F' and s[1]==t[1]:
    print(abs(int(s[0])-int(t[0])))

elif s[1]=='F' and s[1]!=t[1]:
    print(abs(int(s[0])-1+int(t[1])-1+1))

elif s[0]=='B' and s[0]==t[0]:
    print(abs(int(s[1])-int(t[1])))

else:
    print(abs(int(s[1])-1+int(t[0])-1+1))
