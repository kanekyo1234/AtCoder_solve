n=int(input())
zisyo={}
count=0
for i in range(n):
    s="".join(sorted(input()))#間を開けないでSORT
    if s in zisyo:
        zisyo[s]+=1
        count+=zisyo[s]
    else:
        zisyo[s]=0
print(count)
