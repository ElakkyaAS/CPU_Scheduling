"""
Non-preemptive Shortest Job First (SJF) scheduling algorithm.
"""


def sjf(processes):
    """
    Run non-preemptive SJF scheduling.

    Parameters:
        processes: list of dictionaries containing:
                   pid, arrival, burst, priority

    Returns:
        (results, gantt)
    """

    # Make a copy so the original input is not modified.
    process_list = [process.copy() for process in processes]

    # Store processes that are not completed yet.
    unfinished = process_list.copy()

    # Store final results.
    results = []

    # Store Gantt chart entries.
    gantt = []

    # CPU starts at time 0.
    current_time = 0

    # Continue until every process is completed.
    while unfinished:

        # Find all processes that have arrived.
        available = [
            process
            for process in unfinished
            if process["arrival"] <= current_time
        ]

        # If no process has arrived, keep the CPU idle.
        if not available:
            next_arrival = min(
                process["arrival"]
                for process in unfinished
            )

            # Record the idle period.
            if current_time < next_arrival:
                gantt.append(
                    ("Idle", current_time, next_arrival)
                )

            # Jump to the next arrival time.
            current_time = next_arrival
            continue

        # Select the process using:
        # 1. Smallest burst time
        # 2. Earlier arrival time
        # 3. Lower PID
        selected = min(
            available,
            key=lambda process: (
                process["burst"],
                process["arrival"],
                process["pid"]
            )
        )

        # Remove the selected process from unfinished processes.
        unfinished.remove(selected)

        # Process starts at the current time.
        start = current_time

        # Non-preemptive SJF runs the process completely.
        completion = start + selected["burst"]

        # Add the process to the Gantt chart.
        gantt.append(
            (selected["pid"], start, completion)
        )

        # Calculate turnaround time.
        turnaround = completion - selected["arrival"]

        # Calculate waiting time.
        waiting = turnaround - selected["burst"]

        # Store the result.
        results.append({
            "pid": selected["pid"],
            "arrival": selected["arrival"],
            "burst": selected["burst"],
            "completion": completion,
            "turnaround": turnaround,
            "waiting": waiting
        })

        # Move the CPU clock forward.
        current_time = completion

    return results, gantt