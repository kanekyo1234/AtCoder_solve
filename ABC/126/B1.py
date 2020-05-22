s=input()
x=int(s[:2])
y=int(s[2:])
#これで桁を取り出すことができる

if 1<=x<=12:
  if 1<=y<=12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1<=y<=12:
    print("YYMM")
  else:
    print("NA")
