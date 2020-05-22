w=str(input())

n=list(w)
w=int(w)
x=0
ans=""
for i in range(len(n)):
    x+=int(n[i])
#print(x)
if x%9!=0:
    ans+=str(x%9)
x=x-x%9

for i in range(x//9):
    ans+=str(9)
#print (int(ans),w)

if w==int(ans):
    #print("DFGH")
    if len(ans)==1:
        print(1,end="")
        print(int(ans)-1)
    elif len(ans)==2:
        print(int(ans[0:1])+1,end="")
        print(int(ans[1:2])-1,end="")
        print()
    else:
        print(int(ans[0:1])+1,end="")
        print(int(ans[1:2]),end="")
        print(int(ans[2:len(ans)]))
else:
    #print("DFG")
    print(int(ans))
