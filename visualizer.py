import matplotlib.pyplot as plt

import csv
import os

def log_performance(filename, algorithm, time_taken, depth):
    """
    Appends a row to the performance log CSV.

    Args:
        filename (str): Path to the CSV file.
        algorithm (str): Name of the algorithm used.
        time_taken (float): Time taken in seconds.
        depth (int): Search depth reached.
    """
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['algorithm', 'time', 'depth'])  # Header
        writer.writerow([algorithm, time_taken, depth])


def plot_performance(metrics):
    """
    metrics: list of dicts with keys - 'algorithm', 'time', 'depth'
    """
    if not metrics:
        print("⚠️ No metrics to plot.")
        return

    algorithms = [m['algorithm'].upper() for m in metrics]
    times = [m['time'] for m in metrics]
    depths = [m['depth'] for m in metrics]

    colors = {'BFS': '#3498db', 'DFS': '#e74c3c', 'A*': '#2ecc71', 'ASTAR': '#2ecc71'}
    unique_algos = sorted(set(algorithms))

    plt.figure(figsize=(8, 5))

    for algo in unique_algos:
        algo_times = [times[i] for i in range(len(metrics)) if algorithms[i] == algo]
        algo_depths = [depths[i] for i in range(len(metrics)) if algorithms[i] == algo]
        plt.plot(
            algo_depths,
            algo_times,
            marker='o',
            linestyle='-',
            label=algo,
            color=colors.get(algo, '#9b59b6')
        )

    plt.title("⏱️ Time vs Depth by Algorithm", fontsize=14, fontweight='bold')
    plt.xlabel("🔍 Search Depth", fontsize=12)
    plt.ylabel("⏳ Time (seconds)", fontsize=12)
    plt.legend(title="Algorithm")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
