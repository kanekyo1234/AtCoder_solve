a=int(input())
sd=10
count=0
if a%2==0:
    for i in range(100):
        count+=a//sd
        sd*=5
    print(count)
else:
    print("0")
    