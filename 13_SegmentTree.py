# recursive

a = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
tree = [0 for _ in range(4*len(a))]

def init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node] 
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

def sum(start, end, node, left, right):
    if left > end or right < start:
        return 0 
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) //2 
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, index, dif):
    if index < start or index > end:
        return 
    tree[node] += dif
    if start == end:
        return
    mid = (start+end) //2 
    update(start, mid, node*2, index, dif)
    update(mid+1, end, node*2+1, index, dif)

init(0, len(a)-1, 1)
print(tree)
print( sum(0, len(a)-1, 1, 0, 12))
print( sum(0, len(a)-1, 1, 3, 8))
update(0, len(a)-1, 1, 5, -5)
print( sum(0, len(a)-1, 1, 3, 8))