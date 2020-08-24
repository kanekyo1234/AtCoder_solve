import collections
h, w, m = map(int, input().split())
a = []
b = []
for i in range(m):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)
a2 = collections.Counter(a)
b2 = collections.Counter(b)
a_max = a2.most_common()
b_max = b2.most_common()

a_ans = []
a_max2 = -1
for i in a_max:
    a_grid, a_count = i
    if a_max2 == -1 or a_max2 == a_count:
        a_max2 = a_count
        a_ans.append(a_grid)
b_ans = []
b_max2 = -1
for i in b_max:
    b_grid, b_count = i
    if b_max2 == -1 or b_max2 == b_count:
        b_max2 = b_count
        b_ans.append(b_grid)
# print(a_ans, b_ans)

for i in a:
    for j in b:
        if i not in a and j not in b:
            print(a_max2+b_max2)
            break
else:
    print(a_max2+b_max2-1)
