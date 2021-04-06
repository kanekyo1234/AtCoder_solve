from itertools import permutations
s = input()
if len(s) <= 8:
    for i in permutations(list(s)):
        i = "".join(i)
        i = int(i)
        if i % 8 == 0:
            print("Yes")
            exit()
    print("No")
    exit()
