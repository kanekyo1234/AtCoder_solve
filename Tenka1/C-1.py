N=int(input())
nn=4/N
w=0

for h in range(1,3501):
    for n in range(1,3501):
        if (nn - 1/h - 1/n)!=0 and nn > (1/h + 1/n):
            w=1/(nn - 1/h - 1/n)z
            print(w)
            if nn==(1/h + 1/n + 1/w):
                print(h,n,w)
                exit()

"""


        print(nn - 1/h - 1/n)
        break
        if nn - 1/h - 1/n!=0:
            w = 1/(nn - 1/h - 1/n )
            print(h,n,w)
            if  1/h + 1/n+ 1/w==nn:
                print(h,n,w)
                break

"""