a,b=map(int,input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
a_div=make_divisors(a)
b_div=make_divisors(b)
ab_div=a_div+b_div
ab_div.sort()
ab=[]
for i in range(len(ab_div)-1):
    if ab_div[i] == ab_div[i+1]:
        ab.append(ab_div[i])
#print(ab)
ans=[ab[0]]
for i in range(1,len(ab)):
    #print(ans)
    jagh=1
    for j in range(1,len(ans)):
        if ab[i]%ans[j] == 0:
            break
    else:
        #print("hg")
        ans.append(ab[i])
print(len(ans))

