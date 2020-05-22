n=int(input())
a=input()
for i in range(50):
    for j in range(50):
        if n==4*i+7*j:
            print("Yes")
            exit()

print("No")
