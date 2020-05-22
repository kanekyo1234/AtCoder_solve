s=list(str(input()))
a="WBWBWWBWBWBW"*3
ans=[i for i in a]
ans1=["Do","Do","Re","Re","Mi","Fa","Fa","So","So","La","La","Si"]
for i in range(len(ans1)):
    if s==ans[i:20+i]:
        print(ans1[i])
        break
    