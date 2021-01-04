#Priority Queue and Heap

import sys
import heapq
#input = sys.stdin.realine

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = 8
arr = [7, 5, 2, 9, 8, 3, 4, 1]

res = heapsort(arr)

for i in range(n):
    print(res[i])

# Tree
# Binary Search Tree: left child < parent < right child
# Tree Traversal: pre-order(root first), in-order(left-root), post-order(right-root)

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    print(node.data, end=" ")
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node != None:
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")

n = 7
tree = {}

data = ["A", "B", "C", "D", "E", "F", "G"]
left_node = ["B", "D", "F", "None", "None", "None", "None"]
right_node = ["C", "E", "G", "None", "None", "None", "None"]

for i in range(n):
    d = data[i]
    l = left_node[i]
    r = right_node[i]
    
    if l == "None":
        l = None
    if r == "None":
        r = None

    tree[d] = Node(d, l, r)

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])
print()

# Bellman-Ford Algorithm
# positive or negative(circulation or not)