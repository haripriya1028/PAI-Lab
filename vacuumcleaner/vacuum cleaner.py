# Vacuum Cleaner using DFS

def is_goal(state):
    return state[1] == 'Clean' and state[2] == 'Clean'


def get_neighbors(state):
    location, A, B = state
    neighbors = []

    if location == 'A':
        if A == 'Dirty':
            neighbors.append((('A', 'Clean', B), "Suck A"))
        neighbors.append((('B', A, B), "Move Right"))

    elif location == 'B':
        if B == 'Dirty':
            neighbors.append((('B', A, 'Clean'), "Suck B"))
        neighbors.append((('A', A, B), "Move Left"))

    return neighbors


def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if is_goal(state):
            return path + [(state, "Goal Reached")]

        if state not in visited:
            visited.add(state)

            for next_state, action in get_neighbors(state):
                stack.append((next_state, path + [(state, action)]))

    return None


# ---- Dynamic Input ----
location = input("Enter vacuum location (A/B): ").upper()
A = input("Enter status of Room A (Dirty/Clean): ").capitalize()
B = input("Enter status of Room B (Dirty/Clean): ").capitalize()

start_state = (location, A, B)

solution = dfs(start_state)

print("\nDFS Solution Path:")
for step in solution:
    print(step)
