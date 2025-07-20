# simulator.py

from solver import bfs, dfs, astar
from explain import generate_explanation
from visualizer import log_performance
import time

def run_simulation(jugs, goal, method):
    print(f"Running {method.upper()} simulation for jugs: {jugs} and goal: {goal}")

    start_time = time.time()

    if method == "BFS":
        path = bfs(jugs, goal)
    elif method == "DFS":
        path = dfs(jugs, goal)
    elif method == "A*":
        path = astar(jugs, goal)
    else:
        raise ValueError("Unsupported method. Choose BFS, DFS, or A*.")

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 4)

    explanation = generate_explanation(path, goal, method)

    if path:
        solution_found = True
    else:
        solution_found = False

    # Log performance
    log_performance(method, jugs, goal, solution_found, elapsed_time, len(path) if path else 0)

    return {
        "solution": path,
        "explanation": explanation,
        "time": elapsed_time,
        "steps": len(path) if path else 0,
        "success": solution_found
    }
