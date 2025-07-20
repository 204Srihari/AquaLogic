import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from flask import Flask, render_template, request
from solver import bfs, dfs, astar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def solve():
    result = None
    if request.method == 'POST':
        try:
            num_jugs = int(request.form['num_jugs'])
            cap1 = int(request.form['cap1'])
            cap2 = int(request.form['cap2'])
            cap3 = request.form.get('cap3')
            capacities = [cap1, cap2]
            if num_jugs == 3 and cap3:
                capacities.append(int(cap3))
            goal_str = request.form['goal'].replace(" ", "")
            goal = tuple(map(int, goal_str.split(','))) if ',' in goal_str else int(goal_str)
            algorithm = request.form['algorithm']

            # Choose algorithm
            solver_func = {'BFS': bfs, 'DFS': dfs, 'A*': astar}.get(algorithm)
            if not solver_func:
                raise ValueError("Invalid algorithm selected.")

            start_state = tuple(0 for _ in capacities)
            start_time = time.time()
            paths = solver_func(start_state, capacities, goal)
            end_time = time.time()

            if not paths or all(len(p) == 0 for p in paths):
                result = {
                    "error": None,
                    "message": "❌ No solution exists for the given configuration.",
                    "capacities": capacities,
                    "goal": goal,
                    "algorithm": algorithm,
                    "time": round(end_time - start_time, 4),
                    "paths": []
                }
            else:
                result = {
                    "error": None,
                    "message": "✅ Solution(s) Found!",
                    "capacities": capacities,
                    "goal": goal,
                    "algorithm": algorithm,
                    "time": round(end_time - start_time, 4),
                    "paths": paths
                }

        except Exception as e:
            result = {"error": f"Error: {str(e)}"}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
