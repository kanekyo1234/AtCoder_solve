#尾上さんやつ

from itertools import chain, product, zip_longest
 
nums = list(input())
s = 0
for ops in product(('', '+'), repeat=len(nums) - 1):
    print(ops)
    exp = ''.join(chain(*zip_longest(nums, ops, fillvalue='')))
    print(exp)
    s += eval(exp)
print(s)

print(eval('678+2//2'))