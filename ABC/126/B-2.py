s=str(input())
a=int(s[0:2])
b=int(s[2:4])

if 1<=a<=12:
    if 1<=b<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1<=b<=12:
        print("YYMM")
    else:
        print("NA")