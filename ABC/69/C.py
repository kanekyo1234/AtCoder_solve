n=int(input())
a=list(map(int,input().split()))
count4=0#4の倍数
count2=0#2の倍数だが4の倍数じゃない
count1=0
for i in range(n):
    if a[i]%4==0:
        count4+=1
    elif a[i]%2==0:
        count2+=1
    else:
        count1+=1
if count2==0:
    if count1<=count4+1:
        print("Yes")
    else:
        print("No")
else:
    if count1<=count4:
        print("Yes")
    else:
        print("No")

    

    
"""
#print(count2)
if 1<=count2:
    if (n-count2//2)//2<=count or n//2<=count:
        print("Yes")
    elif count2%2==0:
        if   (n-count2)//2<count :
            print("Yes ")
        else:
            print("No")
    elif count2%2==1:
        if  (n-count2)//2<=count :
            print("Yes ")
        else:
            print("No")
else:
    if n//2<=count:
        print("Yes")
    else:
        print("No")

    """
"""    7
    2 2 2 2 3 4 3

    YES になる間違い13晩のテキスト

"""
