s = list(input())
k = int(input())

for i in range(len(s)):
    a = 26-(ord(s[i])-97)
    # print(ord(s[i]))
    # print(a)
    if k >= a and a != 26:
        k -= a
        s[i] = "a"
# print(k)
s[-1] = chr(ord(s[-1]) + k % 26)
# print(ord(s[-1]))
print("".join(s))
