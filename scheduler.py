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

    # --------------------------------------------------
    # Step 1: Get number of processes
    # --------------------------------------------------

    while True:
        try:
            n = int(input("Enter the number of processes: "))

            if n >= 1:
                break

            print("Number of processes must be at least 1.")

        except ValueError:
            print("Please enter an integer.")

    # --------------------------------------------------
    # Step 2: Get process details
    # --------------------------------------------------

    processes = []

    for i in range(n):

        pid = f"P{i + 1}"

        print(f"\nEnter details for {pid}")

        # Arrival time
        while True:
            try:
                arrival = int(
                    input(f"Enter arrival time for {pid}: ")
                )

                if arrival >= 0:
                    break

                print("Arrival time must be 0 or greater.")

            except ValueError:
                print("Please enter an integer.")

        # Burst time
        while True:
            try:
                burst = int(
                    input(f"Enter burst time for {pid}: ")
                )

                if burst > 0:
                    break

                print("Burst time must be greater than 0.")

            except ValueError:
                print("Please enter an integer.")

        # Priority
        while True:
            try:
                priority_value = int(
                    input(f"Enter priority for {pid}: ")
                )

                break

            except ValueError:
                print("Please enter an integer.")

        # Create process dictionary
        process = {
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority_value
        }

        processes.append(process)

    # --------------------------------------------------
    # Step 3: Get time quantum
    # --------------------------------------------------

    while True:
        try:
            quantum = int(input("Enter time quantum: "))

            if quantum > 0:
                break

            print("Time quantum must be greater than 0.")

        except ValueError:
            print("Please enter an integer.")

    # --------------------------------------------------
    # Step 4: Display input process table
    # --------------------------------------------------

    print("\n")
    print("=" * 55)
    print("                 INPUT PROCESS TABLE")
    print("=" * 55)

    print(
        f"{'PID':<10}"
        f"{'Arrival':<12}"
        f"{'Burst':<12}"
        f"{'Priority':<12}"
    )

    print("-" * 55)

    for process in processes:

        print(
            f"{process['pid']:<10}"
            f"{process['arrival']:<12}"
            f"{process['burst']:<12}"
            f"{process['priority']:<12}"
        )

    print("-" * 55)

    print(f"Time Quantum: {quantum}")

    print("=" * 55)

    # --------------------------------------------------
    # Step 5: Run scheduling algorithms
    # --------------------------------------------------

    fcfs_results, fcfs_gantt = fcfs(processes)

    sjf_results, sjf_gantt = sjf(processes)

    rr_results, rr_gantt = round_robin(
        processes,
        quantum
    )

    priority_results, priority_gantt = priority(processes)

    # --------------------------------------------------
    # Step 6: Store all results
    # --------------------------------------------------

    all_results = {
        "FCFS": fcfs_results,
        "SJF": sjf_results,
        "Round Robin": rr_results,
        "Priority": priority_results
    }

    # --------------------------------------------------
    # Step 7: Store all Gantt charts
    # --------------------------------------------------

    all_gantts = {
        "FCFS": fcfs_gantt,
        "SJF": sjf_gantt,
        "Round Robin": rr_gantt,
        "Priority": priority_gantt
    }

    # --------------------------------------------------
    # Step 8: Display results for each algorithm
    # --------------------------------------------------

    print("\n")
    print("=" * 55)
    print("                 SCHEDULING RESULTS")
    print("=" * 55)

    print_results("FCFS", fcfs_results)

    print_results("SJF", sjf_results)

    print_results("Round Robin", rr_results)

    print_results("Priority", priority_results)

    # --------------------------------------------------
    # Step 9: Display comparison
    # --------------------------------------------------

    print("\n")
    print("=" * 55)
    print("                 ALGORITHM COMPARISON")
    print("=" * 55)

    print_comparison(all_results)

    # --------------------------------------------------
    # Step 10: Find best algorithm
    # --------------------------------------------------

    print("\n")
    print("=" * 55)
    print("                   BEST ALGORITHM")
    print("=" * 55)

    best_algorithm(all_results)

    # --------------------------------------------------
    # Step 11: Display Gantt charts
    # --------------------------------------------------

    print("\n")
    print("=" * 55)
    print("                    GANTT CHARTS")
    print("=" * 55)

    plot_gantt(all_gantts)


# ------------------------------------------------------
# Program starts here
# ------------------------------------------------------

if __name__ == "__main__":
    main()
