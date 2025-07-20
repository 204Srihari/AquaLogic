# main.py

import argparse
from simulator import run_simulation
from web_app.app import launch_web_ui

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SmartJugAI: Water Jug Solver")
    parser.add_argument("--mode", choices=["cli", "web"], default="cli", help="Select mode: cli or web")
    args = parser.parse_args()

    if args.mode == "web":
        launch_web_ui()
    else:
        run_simulation()
