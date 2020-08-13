print("日本語を入力してください：", end="")
s = input()
while 0 < len(s):
    if s[-5:] == 'erase' or s[-5:] == 'dream':
        s = s[0:-5]
    elif s[-6:] == 'eraser':
        s = s[0:-6]
    elif s[-7:] == 'dreamer':
        s = s[0:-7]
    else:
        print("NO")
        exit()
print("YES")
