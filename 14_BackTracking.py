### template

def is_valid_state(state):
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
    # return
    
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)
        
def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solution

### N - Queens

def solve():
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions

def is_valid_state(state, n):
    return len(state) == n

def get_candidates(state, n):
    if not state:
        return range(n)
    
    position = len(state)
    candidates = set(range(n))
            
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates

def search(state, solutions, n):
    if is_valid_state(state, n):
        state_string = state_to_string(state, n)
        solutions.append(state_string)
        return
    
    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()
            
def state_to_string(state, n):
    ret = []
    for i in state:
        string = '.' * i + 'Q' + '.' * (n-i-1)
        ret.append(string)
    return ret

n = 5      

print(solve())