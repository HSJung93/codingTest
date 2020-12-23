def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = ( start + end ) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid-1)
    else:
        return binary_search_recursive(array, target, mid+1, end)

n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search_recursive(array, target, 0, n-1)
if result == None:
    print("There is NO target.")
else:
    print(result + 1)

def binary_search_iterative(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search_recursive(array, target, 0, n-1)
if result == None:
    print("There is NO target.")
else:
    print(result + 1)

from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1 ,3 ))


n, m = 4, 6
array = [19, 15, 10 ,17]
start = 0
end = max(array) 

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result) 

from bisect import bisect_left, bisect_right
n, x = 7, 2
array = [1, 1, 2, 2, 2, 2, 3]

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)