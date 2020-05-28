n, a, b = map(int,input().split())
s = list(str(input()))
a_Yes = 0
b_Yes = 0

for i in range(n):
    if s[i] == "a":
        if  a_Yes + b_Yes <a+b:
            print("Yes")
            a_Yes += 1
        else:
            print("No")

    elif s[i] == "b" :
        if b_Yes < b and  a_Yes + b_Yes <a+b:
            print("Yes")
            b_Yes += 1
        else:
            print("No")

    else:
        print("No")
