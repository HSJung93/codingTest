import sys
sys.setrecursionlimit(10 ** 6)

############# String

def solution(s):
    length = []
    result = ''

    if len(s) == 1:
        return 1

    for cut in range(1, len(s) // 2 + 1):
        cnt = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + tempStr
                tempStr = s[i:i+cut]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + tempStr
        length.append(len(result))
        result = ''
    
    return min(length)


############# Difference of Strings in List

for word_2_idx in range(len(words)-1, -1, -1):
    word_2 = words[word_2_idx]
    difference = sum([x != y for x, y in zip(word_1, word_2)])
    # 차이가 1이면
    if difference == 1:
        tmp_q.append(words.pop(word_2_idx))

############# Greedy

def change(i):
    if i == "*":
        return 10
    elif i == 0:
        return 11
    elif i == "#":
        return 12
    return i

def dist(i, j):
    i = change(i)
    j = change(j)
    
    ix = (i-1)//3 
    iy = (i-1)%3
    jx = (j-1)//3
    jy = (j-1)%3

    return abs(ix-jx) + abs(iy-jy)


def solution(numbers, hand):
    answer = ''
    leftWhere = "*"
    rightWhere = "#"
    alwaysLeft = [1, 4, 7]
    alwaysRight = [3, 6, 9]
    closeOne = [2, 5, 8, 0]
    for i in numbers:
        if i in alwaysLeft:
            answer = answer + "L"
            leftWhere = i
        elif i in alwaysRight:
            answer = answer + "R"
            rightWhere = i
        else:
            if dist(i,leftWhere) < dist(i,rightWhere):
                answer = answer + "L"
                leftWhere = i
            elif dist(i,leftWhere) > dist(i,rightWhere):
                answer = answer + "R"
                rightWhere = i
            else:
                if hand == "left":
                    answer = answer + "L"
                    leftWhere = i
                else:
                    answer = answer + "R"
                    rightWhere = i                         
    return answer

############# String

import re
from collections import defaultdict

def isRight(s):
    while "()" in s:
        s = s.replace("()","")

    if s == "":
        return True
    else:
        return False

def makeBalance(s):
    dt = defaultdict(int)
    cut = 0
    for i in range(len(s)):
        dt[s[i]] += 1
        if dt['('] == dt[')']:
            cut = i
            break
    return s[:cut+1], s[cut+1:]

def flip(s):
    if s == "":
        return ""
    t = ""
    for i in s:
        if i == "(":
            t += ")"
        else:
            t += "("
    return t

def solution(p):
    answer = ''
    if p == "":
        return ""
    u, v = makeBalance(p)

    if isRight(u) == True:
        return u + solution(v)
    
    else:
        return "(" + solution(v) + ")" + flip(u[1:-1])
  
  
############# BFS

import math
from collections import deque

def bfs(start, board):
    table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]
    dirs = [(-1,0),(0,-1),(1,0),(0,1)] #위0 왼1 아2 오3
    queue = deque([start])
    
    table[0][0] = 0
    while queue:
        x, y, cost, head = queue.popleft()
        for idx, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y+ dy
            n_cost = cost + 600 if idx != head else cost + 100
            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0 and table[nx][ny] > n_cost:
                table[nx][ny] = n_cost
                queue.append((nx, ny, n_cost, idx))
    return table[-1][-1]
            
def solution(board):
    answer = min(bfs((0, 0, 0, 2), board), bfs((0,0,0,3), board))
    return answer
  
  
########### Two pointer

def solution(gems):
    whole = set(gems)
    dic = {}
    dic[gems[0]] = 1

    l = 0
    r = 0

    answer = [0, len(gems)-1]

    while l <len(gems) and r <len(gems):
        if len(dic) == len(whole):
            # if dic[gems[l]] == 1:
                # del dic[gems[l]]
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else: dic[gems[l]] -= 1
            l += 1
        else:
            r += 1
            if r == len(gems):
                break
            if gems[r] in dic.keys():
                dic[gems[r]] += 1
            else:
                dic[gems[r]] = 1
    
    answer[0] = answer[0] + 1
    answer[1] = answer[1] + 1

    return answer
  
  ########### DFS2 #############
  from collections import deque

def solution(n, path, order):
    answer = True
    adj = {n: [] for n in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)
    
    preA = {}
    preB = {}

    for a, b in order:
        preA[a] = b
        preB[b] = a
        if b == 0:
            return False
        if a == 0:
            preA[0] = 0

    visited = [0] * n
    visited[0] = 1

    q = deque() 
    q.append(0)

    while q:
        current = q.popleft()
        if current == preA.get(preB.get(current)):
            visited[current] = 2
        else:
            for neighbor in adj[current]:
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

                    if preA.get(neighbor):
                        if visited[preA[neighbor]] == 2:
                            q.append(preA[neighbor])
                            visited[preA[neighbor]] = 1
                        preA[neighbor] = 0

    for i in visited:
        if i == 0:
            return False
    return answer
