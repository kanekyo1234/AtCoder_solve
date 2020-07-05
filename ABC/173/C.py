import copy
from itertools import product


h, w, k = map(int, input().split())
c = [list(input()) for i in range(h)]
ans = 0
for x in product((0, 1), repeat=h):
    for y in product((0, 1), repeat=w):
        b = copy.deepcopy(c)
        for i in range(h):
            if x[i] == 1:
                for tate in range(w):
                    # print(tate)
                    b[i][tate] = "S"

        for j in range(w):
            if y[j] == 1:
                for yoko in range(h):
                   # print(yoko, j)
                    b[yoko][j] = "S"
        count = 0
        for i in range(h):
            count += b[i].count("#")

        if count == k:
            ans += 1
print(ans)


# for i in range(h):
#     for j in range(w):

#         count=0
#         for x in range(h):
#             b[i][x]="S"
#         for y in range(w):
#             b[y][j]
