a=int(input())
c=a%100
b=a//100
if 1<=b<=12:
    if 1<=c<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1<=c<=12:
        print("YYMM")
    else:
        print("NA")