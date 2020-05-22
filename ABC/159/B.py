s=str(input())
a1=s[::-1]
if s!=a1:
    print("No")
    exit()
n=len(s)
a2=s[0:(n-1)//2]
#print(a2)
a21=a2[::-1]

if a2!=a21:
    print("No")
    exit()

a3=s[(n+3)//2-1:n]
#print(a3)
a31=a3[::-1]
if a3!=a31:
    print("No")
    exit()
print("Yes")