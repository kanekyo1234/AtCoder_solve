sa=list(str(input()))
sb=list(str(input()))
sc=list(str(input()))
ac,bc,cc=0,0,0
sa.append("g")
sb.append("g")
sc.append("g")
now =1
while ac<len(sa) and bc<len(sb) and cc<len(sc):
    if now ==1:#A
        if sa[ac]=='b':
            now=2
        elif sa[ac]=='c':
            now=3
        elif sa[ac]=='g':
            print("A")
            break
        ac+=1
    elif now == 2:#B
        if sb[bc]=='a':
            now=1
        elif sb[bc]=='c':
            now=3
        elif sb[bc]=='g':
            print("B")
            break
        
        bc+=1
    else:#C
        if sc[cc]=='a':
            now=1
        elif sc[cc]=='b':
            now=2
        elif sc[cc]=='g':
            print("C")
            break

        cc+=1