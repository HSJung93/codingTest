# Use PyPy if possible it much faster
# s: 1 n: 2k -> o(n^2) // s: 1 n: 100k -> o(nlogn)

# float comparison error
## example
a = 0.3 + 0.6
print(a)
print(True) if a == 0.9 else print(False)
## Use round(value, digit)
print(round(a, 4))
print(True) if round(a, 4) == 0.9 else print(False)

# making 0 vector list
n = 10
a = [0] * n
print(a)

# list comprehension 
## % is remainder // is share
array = [i for i in range(10) if i % 2 == 1 ]
print(array)
n = 4
m = 3 # 5 * 3
twoDimArr1 = [[0] * m for _ in range(n)]
twoDimArr2 = [[0] * m ] * n
twoDimArr1[1][1] = 2
print(twoDimArr1)
twoDimArr2[1][1] = 3
print(twoDimArr2)

## sort() reverse() insert() count() remove()
array.insert(2, 1)
array.insert(-1, 9)
print(array)
array.remove(1)
print(array) # only remove one 
remove_set = {9}
arrayAllRemoved = [ i for i in array if i not in remove_set]
print(arrayAllRemoved)

# tuple (cost, nodeNumber) in shortest path , in hasing key value

# dictionary
dic = dict()
dic["k1"] = "v1"
dic["k2"] = "v2"
dic["k3"] = "v3"
key_list = list(dic.keys())
value_list = dic.values()
print(key_list)
for key in key_list:
    print(dic[key], end=" ")
print("\n")

# set
arr1 = set([1,2,3])
arr2 = {2,3}
arr2.update([4])
arr2.add(5)
arr2.remove(5)
print(arr2)

# input number
# inp = list(map(int, input().split()))
# print(inp)
# a, b = map(int, input().split())
# print(a, b)
## faster with sys
# import sys 
# data = sys.stdin.readline().rstrip()
# print(data)

# fstring
answer = 7
print(f"The answer is {answer}.")

# and or
if True and False:
    print("TaF")
if True or False:
    print("ToF")

# using continue
scores = [90, 85, 77, 65, 97]
excepted = {2, 4}

for i in range(len(scores)):
    if i + 1 in excepted:
        continue
    if scores[i] > 80:
        print(i+1, "'s student passed the test.")

# lambda
print((lambda x, y: x+y)(2, 7))
## lambda with sorted with key
array = [("a",3),("b",1),("c",2)]
print(sorted(array, key=lambda x: x[1]))
## lambda with lists
l1 = [i for i in range(1, 6)]
l2 = [i for i in range(5, 0, -1)]
sum12 = map(lambda a, b: a+b, l1, l2)
a, b, c, d, e = map(lambda a, b: a+b, l1, l2)
print(a, b)
print(list(sum12))

# library!
print(eval("(3-7)*3"))
## itertools
data = ["a", "b", "c"]
from itertools import permutations, combinations, product, combinations_with_replacement
### combinations
print(list(permutations(data, 2)))
### permutations
print(list(combinations(data, 2)))
### combinations with replacement
print(list(combinations_with_replacement(data, 2)))
### permutations with replacement
print(list(product(data, repeat=2)))

## heapq : heap, que first
## bisect : binary search
## collections : deque, counter
from collections import Counter

counter = Counter(['r','b','r','g','b','b'])
print(counter['b'])
print(dict(counter))
## math
import math 
def lcm(a, b): 
    return a * b // math.gcd(a, b)
a = 21
b = 14
print(math.gcd(21, 14))
print(lcm(21, 14)) 