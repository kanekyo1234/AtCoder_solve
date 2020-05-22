s=str(input())

for i in range(26):
    if s.count(chr(97+i))==0:
        print(chr(97+i))
        break
else:
    print("None")
