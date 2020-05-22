s=list(str(input()))
a=[2,4,5,7,9]
b=[0,1,6,8]
if int(s[-1]) in a:
    print("hon")
elif int(s[-1]) in b:
    print("pon")
else:
    print("bon")