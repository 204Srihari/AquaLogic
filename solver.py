from collections import deque
import heapq

def is_goal(state, goal):
    if isinstance(goal, tuple):
        return state == goal
    return goal in state

def get_next_states(state, capacities):
    n = len(capacities)
    next_states = []
    for i in range(n):
        # Fill
        if state[i] < capacities[i]:
            next = list(state)
            next[i] = capacities[i]
            next_states.append((tuple(next), f"Fill Jug {i+1}"))
        # Empty
        if state[i] > 0:
            next = list(state)
            next[i] = 0
            next_states.append((tuple(next), f"Empty Jug {i+1}"))
        # Pour
        for j in range(n):
            if i != j and state[i] > 0 and state[j] < capacities[j]:
                next = list(state)
                pour_amt = min(state[i], capacities[j] - state[j])
                next[i] -= pour_amt
                next[j] += pour_amt
                next_states.append((tuple(next), f"Pour Jug {i+1} → Jug {j+1}"))
    return next_states

def bfs(start, capacities, goal):
    queue = deque()
    visited = set()
    queue.append((start, []))
    visited.add(start)
    while queue:
        current, path = queue.popleft()
        if is_goal(current, goal):
            return path + [(current, "Goal Reached")]
        for next_state, action in get_next_states(current, capacities):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(current, action)]))
    return None

def dfs(start, capacities, goal, max_depth=1000):
    stack = [(start, [], 0)]
    visited = set()
    while stack:
        current, path, depth = stack.pop()
        if current in visited or depth > max_depth:
            continue
        visited.add(current)
        if is_goal(current, goal):
            return path + [(current, "Goal Reached")]
        for next_state, action in reversed(get_next_states(current, capacities)):
            if next_state not in visited:
                stack.append((next_state, path + [(current, action)], depth + 1))
    return None

def heuristic(state, goal):
    if isinstance(goal, tuple):
        return sum(abs(state[i] - goal[i]) for i in range(len(goal)))
    return min(abs(x - goal) for x in state)

def astar(start, capacities, goal):
    heap = []
    visited = set()
    heapq.heappush(heap, (0 + heuristic(start, goal), 0, start, []))
    while heap:
        f, cost, current, path = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        if is_goal(current, goal):
            return path + [(current, "Goal Reached")]
        for next_state, action in get_next_states(current, capacities):
            if next_state not in visited:
                new_cost = cost + 1
                priority = new_cost + heuristic(next_state, goal)
                heapq.heappush(heap, (priority, new_cost, next_state, path + [(current, action)]))
    return None

# ✅ WRAPPER CLASS FOR WEB AND CLI
class WaterJugSolver:
    def __init__(self, capacities, goal, strategy='BFS'):
        self.capacities = capacities
        self.goal = goal
        self.strategy = strategy.upper()

    def solve(self):
        start = tuple([0] * len(self.capacities))
        if self.strategy == "BFS":
            return bfs(start, self.capacities, self.goal)
        elif self.strategy == "DFS":
            return dfs(start, self.capacities, self.goal)
        elif self.strategy == "A*":
            return astar(start, self.capacities, self.goal)
        else:
            raise ValueError("Unknown strategy: " + self.strategy)
