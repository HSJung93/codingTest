# Here's Change
n = 1260
count = 0
## Monetary units
arr = [500, 100, 50, 10]

for coin in arr:
    count += n // coin
    n %= coin
print(count)

# Until One
n, k = 17, 4 
# map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result) 

# Multiply or Plus
data = "14312512"
#input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# Scary Adventurer

data = [4, 3, 2, 4, 2, 1, 1, 2, 3, 1, 2, 2, 2]
# list(map(int, input().split()))
n = len(data)
# int(input())
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# Implementation
for i in range(5):
    for j in range(5):
        print( "(", i, ",", j, ")", end=" ")
    print()

n = 5
# int(input()) 
x, y = 1, 1
plans = "RRRUDD"
# input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mv = ['L', 'R', 'U', 'D']

for p in plans:
    for i in range(len(mv)):
        if p == mv[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

# Time with 3
h = 12
# int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1
print(count)

# Knight
input_data = "a1"
## input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]

    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        result += 1
print(result)

# Some sort
data = "A5BHDFG45B3D2G8"
## input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))