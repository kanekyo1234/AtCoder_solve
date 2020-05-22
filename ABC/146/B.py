n= int(input())
b=list(map(str,input()))
for i in range(0,len(b),1):
    b[i]=ord(b[i])+n
    if b[i]>90 :
        b[i]-=26
    print(chr(b[i]),end="")