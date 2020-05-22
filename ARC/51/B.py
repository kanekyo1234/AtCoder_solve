a=int(input())

fib=[0,1]
for i in range(a):
    fib.append(fib[i]+fib[i+1])
print(fib[-2],fib[-1])