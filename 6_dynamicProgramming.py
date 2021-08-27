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

# gridTraveler
# 메모가 없는 버전에서 1. 재귀 처음에서 메모 값이 없을 경우 채워 넣는다. 2. 리턴 위에서 메모 값으로 계산
def gridTraveler(m, n, memo):
    if memo[m][n] != -1: 
        return memo[m][n]
    if m == 1 and n == 1: 
        return 1
    if m == 0 or n == 0: 
        return 0
    memo[m][n] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[m][n]

m, n = 30, 30

memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]

print(gridTraveler(m, n, memo))

#canSum: Can you do it? yes/no -> decision problem
#메모 빈 defaultdict을 전달하는것도 상당히 편리
from collections import defaultdict

def canSum(target, num_list, memo):
    if target in memo: return memo[target]
    if target == 0: return True
    if target <0: return False
    
    for num in num_list:
        remainder = target - num
        if canSum(remainder, num_list, memo):
            memo[target] = True
            return True
        
    memo[target] = False
    return False

memo = defaultdict(bool)
print(canSum(7, [2, 3], memo))
memo = defaultdict(bool)
print(canSum(7, [5, 3, 4, 7], memo))
memo = defaultdict(bool)
print(canSum(7, [2, 4], memo))
memo = defaultdict(bool)
print(canSum(8, [2, 3, 5], memo))
memo = defaultdict(bool)
print(canSum(300, [7, 14], memo))

#howSum: how will you do it? -> combinatoric problem
from collections import defaultdict

def howSum(target, num_list, memo):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for num in num_list:
        remainder = target - num
        remainderResult = howSum(remainder, num_list, memo)
        if remainderResult != None:
            remainderResult.append(num)
            memo[target] = remainderResult
            return memo[target]

    memo[target] = None
    return memo[target]

memo = defaultdict(bool)
print(howSum(7, [2, 3], memo))
memo = defaultdict(bool)
print(howSum(7, [5, 3, 4, 7], memo))
memo = defaultdict(bool)
print(howSum(7, [2, 4], memo))
memo = defaultdict(bool)
print(howSum(8, [2, 3, 5], memo))
memo = defaultdict(bool)
print(howSum(300, [7, 14], memo))

#bestSum: what is the best way to do it? -> optimization problem
from collections import defaultdict

def bestSum(target, num_list, memo):
    if target in memo: return memo[target]
    if target == 0: return []
    if target <0 : return None

    # 자녀 노드의 길이를 비교한 후 값을 결정한다.
    shortestRemainderResult = None

    for num in num_list:
        remainder = target-num
        remainderResult = bestSum(remainder, num_list, memo)
        if remainderResult != None:
            remainderResult.append(num)
            if (shortestRemainderResult == None or len(remainderResult) < len(shortestRemainderResult)):
                shortestRemainderResult = remainderResult  


    memo[target] = shortestRemainderResult
    return memo[target]


memo = defaultdict(bool)
print(bestSum(7, [2, 3], memo))
memo = defaultdict(bool)
print(bestSum(7, [5, 3, 4, 7], memo))
memo = defaultdict(bool)
print(bestSum(7, [2, 4], memo))
memo = defaultdict(bool)
print(bestSum(8, [2, 3, 5], memo))
memo = defaultdict(bool)
print(bestSum(300, [7, 14], memo))

#canConstruct
from collections import defaultdict

def canConstruct(target, wordBank, memo):
    if target in memo: return memo[target]
    if target == "": return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                # 이곳에서 memo[target]를 리턴할 필요는 없다. 재귀 차원에 들어갔을 때에 메모를 확인하고, 값이 나왔을 때 저장하는 것이 메모이제이션이다. 
                return True

    # False는 모든 경우를 따져본 후에 결정된다. 재귀에서 가장 높은 차원에서 그러하고, 재귀 속에서도 그러할 것이다.
    memo[target] = False
    return False


memo = defaultdict(bool)
print(canConstruct("abcdef", ["ab","abc","cd","def","abcd"], memo))
memo = defaultdict(bool)
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "sks", "sk", "boar"], memo))
memo = defaultdict(bool)
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo))
memo = defaultdict(bool)
print(canConstruct("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee"], memo))