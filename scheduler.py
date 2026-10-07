"""
CPU Scheduling Simulator

This program takes process details as input and runs
FCFS, SJF, Round Robin, and Priority scheduling algorithms.
"""

from fcfs import fcfs
from sjf import sjf
from rr import round_robin
from priority import priority

from output import (
    print_results,
    print_comparison,
    best_algorithm,
    plot_gantt
)


def main():
    """Get input, run scheduling algorithms, and display results."""

    # Step 1: Get the number of processes
    while True:
        try:
            n = int(input("Enter the number of processes: "))

            if n >= 1:
                break

            print("Number of processes must be at least 1.")

        except ValueError:
            print("Please enter an integer.")

    # Step 2: Create the process list
    processes = []

    for i in range(n):
        pid = f"P{i + 1}"

        print(f"\nEnter details for {pid}")

        # Get arrival time
        while True:
            try:
                arrival = int(input(f"Enter arrival time for {pid}: "))

                if arrival >= 0:
                    break

                print("Arrival time must be 0 or greater.")

            except ValueError:
                print("Please enter an integer.")

        # Get burst time
        while True:
            try:
                burst = int(input(f"Enter burst time for {pid}: "))

                if burst > 0:
                    break

                print("Burst time must be greater than 0.")

            except ValueError:
                print("Please enter an integer.")

        # Get priority
        while True:
            try:
                priority_value = int(input(f"Enter priority for {pid}: "))
                break

            except ValueError:
                print("Please enter an integer.")

        # Create the process dictionary
        process = {
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority_value
        }

        # Add the process to the list
        processes.append(process)

    # Step 3: Get the time quantum
    while True:
        try:
            quantum = int(input("Enter time quantum: "))

            if quantum > 0:
                break

            print("Time quantum must be greater than 0.")

        except ValueError:
            print("Please enter an integer.")
          # Step 4: Print the input process table
    print("\nInput Process Table")
    print("-" * 45)
    print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}")
    print("-" * 45)

    for process in processes:
        print(
            f"{process['pid']:<10}"
            f"{process['arrival']:<10}"
            f"{process['burst']:<10}"
            f"{process['priority']:<10}"
        )

    print("-" * 45)


if __name__ == "__main__":
    main()
