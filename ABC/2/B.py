w=list(str(input()))
wa=['a','i','u','e','o']
ans=[]
for i in range(len(w)):
    if w[i] not in wa:
        ans.append(w[i])
for i in range(len(ans)):
    print(ans[i],end="")
print()
"""
a=""
for s in input():
    if s not in "aiueo":
        a+=s
print(a)

"""