n, m = map(int,input().split())
h = list(map(int,input().split()))
n_ans=[1]*n

for i in range(m):
    a, b = map(int,input().split())
    if h[a-1] <= h[b-1] and n_ans[a-1] == 1:
        n_ans[a-1] = 0
    if h[b-1] <= h[a-1] and n_ans[b-1] == 1:
        n_ans[b-1] = 0
print(sum(n_ans))

knai
