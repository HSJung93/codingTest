#Disjoint
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_parent_pc(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_pc(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 6, [[1, 4], [2, 3], [2, 4], [5, 6]]
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in e:
    a, b = i
    union_parent(parent, a, b)

print('The set which the elements is in: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

print('The parent\'s table: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

#Cycle
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in e:
    a, b = i 
    if find_parent_pc(parent, a) == find_parent_pc(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("There exists cycle")
else:
    print("There is no cycle")

#Minimum Spanning Tree
#Kruskal Algorithm
v = 7
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

c = [[1, 2, 29], [1, 5, 75], [2, 3, 35], [2, 6, 34], [3, 4, 7], [4, 6, 23], [4, 7, 13], [5, 6, 53], [6, 7, 25]]

for i in c:
    a, b, cost = i
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent_pc(parent, a) != find_parent_pc(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

#Topological Sorting
from collections import deque

v, e = 7, 8
indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

e = [[1,2],[1,5],[2,3],[2,6],[3,4],[4,7],[5,6],[6,4]]

for i in e:
    a, b = i
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()