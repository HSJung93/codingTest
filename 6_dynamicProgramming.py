#fibonacci
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(6))

#antWarrior
#a_i = max(a_(i-1), a_(i-2)+k_i)
n = 4
array = [1, 3, 1, 5] 
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])

#makingOne
#a_i = max(a_(i-1), a_(i/2), a_(i/3), a_(i/5)) + 1

x = 26
d= [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])

#composePenny
n, m = 2, 15
array = [2, 3]

d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

#goldMine
#dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
T = 2
n1, m1 = 3, 4
arr1 = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
n2, m2 = 4, 4
arr2 = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]

dp = []
index = 0

for i in range(n1):
    dp.append(arr1[index:index+m1])
    index += m1

for j in range(1, m1):
    for i in range(n1):
        if i==0: left_up = 0
        else: left_up = dp[i-1][j-1]
        if i==(n1-1): left_down = 0
        else: left_down = dp[i+1][j-1]
        left = dp[i][j-1]

        dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n1):
        result = max(result, dp[i][m1-1])
print(result)

#arrangeSoldiers
#longestIncresingSubsequence
#0<=j<i, d[i] = max(d[i], d[j]+1) if array[j] < array[i]

n = 7
array = [4, 2, 5, 8, 4, 11, 15] 
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(dp[i], dp[j]+1)

print(n-max(dp))