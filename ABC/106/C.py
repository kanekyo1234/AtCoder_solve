s=int(input())
k=int(input())

for i in range(min(len(str(s)),k)):
    if str(s)[i]!='1':
        print(str(s)[i])
        exit()
print(1)
   