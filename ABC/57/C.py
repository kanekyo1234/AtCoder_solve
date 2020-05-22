n=int(input())


ma=int(n**0.5)
#print(ma)
for i in range(ma,0,-1):
    if n%i==0:
        print(max(len(str(i)),len(str(n//i))))
        break