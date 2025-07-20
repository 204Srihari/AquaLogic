# utils.py

def is_valid_state(capacities, goal):
    if isinstance(goal, int):
        return goal <= max(capacities)
    elif isinstance(goal, tuple):
        return all(g <= c for g, c in zip(goal, capacities))
    return False

def parse_goal_input(raw_input, num_jugs):
    raw = raw_input.strip()
    if "," in raw or "(" in raw:
        try:
            goal = tuple(map(int, raw.replace("(", "").replace(")", "").split(",")))
            if len(goal) != num_jugs:
                raise ValueError("Goal length mismatch.")
            return goal
        except Exception:
            raise ValueError("Invalid tuple goal format.")
    else:
        try:
            return int(raw)
        except Exception:
            raise ValueError("Invalid goal format.")

def state_to_str(state):
    return "(" + ", ".join(map(str, state)) + ")"

def format_action(action):
    return f" → {action}" if action else ""

def log_to_csv(log_path, row):
    import csv
    from os.path import exists
    header = ["Capacities", "Goal", "Algorithm", "Steps", "Time (s)", "Status"]
    write_header = not exists(log_path)

    with open(log_path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow(row)
