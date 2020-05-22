s=str(input())
t=int(input())

x=abs(s.count('R')-s.count('L'))
y=abs(s.count('D')-s.count('U'))
if t==1:
    print(x+y+s.count('?'))
else:
    if x+y<s.count('?'):
        print(abs(x+y-s.count('?'))%2)
    else:
        print(abs(x+y-s.count('?')))