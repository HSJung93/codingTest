

### stack
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::1])
print(stack)

### queue
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

### recursive function
def recursive_function(i):

    if i == 10:
        return
    print("from", i, "'th recursive function call", i+1, "recursive function." )
    recursive_function(i + 1)
    print("end", i, "'th recursive function.")

recursive_function(2)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))

# euclidean algorithm
def gcd(a, b):
    if a % b ==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192, 162))

###dfs method
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
print()
### bfs method
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 7],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1 ,visited)
print()
### icing icecream

n, m = 4, 5

inp = ["00110", "00011", "11111", "00000"]

graph = []
for i in range(n):
    graph.append(list(map(int, inp[i])))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True 
    return False   

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

### shortest path of a maze
from collections import deque
n, m = 5, 6

inp = ["101010", "111111", "000001", "111111", "111111"]

graph=[]
for i in range(n):
    graph.append(list(map(int, inp[i])))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue 

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1] 

print(bfs(0, 0))