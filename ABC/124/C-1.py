S=input()

a = ''
b = ''
s_len = len(S)
for i in range(s_len):
        if (i % 2 == 0):
                a += '1'
                b += '0'
        else :
                a += '0'
                b += '1'


c1,c2 = 0,0
for j in range(s_len):
        if (a[j] != S[j]):
                c1 += 1
        if (b[j] != S[j]):
            c2 += 1

print(min(c1,c2))
