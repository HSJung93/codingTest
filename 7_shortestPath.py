#DijkstraAlgorithm
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = 6, 11
start = 1
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

graph = [
    [],
    [(2, 2), (3, 3), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]

# return unvisited node index which is shortest
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # distance of start node is 0
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

#priorityQueue and Heap
import heapq

#heapSort
def minHeap(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def maxHeap(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

mess = [1, 3, 5, 7, 9 ,2, 4, 6, 8, 0]
minh = minHeap(mess)
maxh = maxHeap(mess)
print(minh)
print(maxh)

def dijkstar_heap(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        # check whether the node is visited 
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstar_heap(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

#FloydWarshall distance from every node to every node
#dynamic algorithm with 2 dimension table 
#D_(ab) = min(D_(ab), D_(ak)+ D_(kb))

n = 4

graph = [
    [],
    [[], 0, 4, INF, 6],
    [[], 3, 0, 7, INF],
    [[], 5, INF, 0, 4],
    [[], INF, INF, 2, 0]
]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

#example
n, m, start= 3, 2, 1

graph = [
    [],
    [(2, 4), (3, 2)],
    [],
    []
]

INF = int(1e9)
distance = [INF] * (n+1)

import heapq
#import sys
#input = sys.stdin.realine

def dijkstra(start):
    q  = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)

#futureCity
n, m = 5, 7
x, k = 4, 5 
graph = [
    [INF,INF,INF,INF,INF,INF],
    [INF, 0, 1, 1, 1, INF],
    [INF, 1, 0, INF, 1, INF],
    [INF, 1, INF, 0, 1, 1],
    [INF, 1, 1, 1, 0, 1],
    [INF, INF, INF, 1, 1,0]
    ]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)