# explain.py

def generate_explanation(path, goal, method):
    explanation = f"Using {method.upper()} search, the algorithm attempted to reach the goal state {goal}.\n\n"
    if not path:
        explanation += "However, no solution was found after exploring all possible states."
    else:
        explanation += f"A solution was found in {len(path) - 1} steps:\n"
        for i, state in enumerate(path):
            explanation += f"Step {i}: {state}\n"
        explanation += "\nEach step involved either filling, emptying, or pouring between jugs."

    return explanation
