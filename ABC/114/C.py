n=int(input())#357の木を作る
a=[]
ans=0

def search(count):
    global ans
    #print(count)
    if int(count)>n:#超えたら終わり
        return 
    #print(set(sorted(list(count))))
    if set(sorted(list(count))) =={"0","3","5","7"}:#lsitにかえてそれをsortしてset型に変える
        ans+=1

    for i in "357":
        search(count+i)


search("0")
print(ans)