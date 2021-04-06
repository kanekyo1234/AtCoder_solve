a,b,x=map(int,input().split())



def binary_search(L,R):
    if L+1>=R:#3,4の時Cenは３になるのでそれ防止
        return L
    else:
        Cen=(L+R)//2
        count=a* Cen + b*len(str(Cen))
        
        if count<x:
            L=Cen
            return binary_search(L,R)
        
        elif count>x:
            R=Cen
            return binary_search(L,R)#return binary_search(Cen,R)の方がいい
        else:
            return Cen

print(binary_search(0,10**9+1))