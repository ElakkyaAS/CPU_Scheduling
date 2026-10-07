"""
Preemptive Shortest Remaining Time First (SRTF) scheduling algorithm.
"""


def srtf(processes):
    """
    Run preemptive SRTF scheduling.

    Parameters:
        processes: list of dictionaries containing:
                   pid, arrival, burst, priority

    Returns:
        (results, gantt)
    """

    # Make a copy so the original input is not modified.
    process_list = [process.copy() for process in processes]

    # Store remaining burst time for each process.
    remaining = {
        process["pid"]: process["burst"]
        for process in process_list
    }

    # Store completion times.
    completion_times = {}

    # Gantt chart.
    gantt = []

    # Number of completed processes.
    completed = 0

    # CPU clock.
    current_time = 0

    while completed < len(process_list):

        # Find processes that have arrived and are not finished.
        available = [
            process
            for process in process_list
            if process["arrival"] <= current_time
            and remaining[process["pid"]] > 0
        ]

        # If nothing has arrived, CPU is idle.
        if not available:

            next_arrival = min(
                process["arrival"]
                for process in process_list
                if remaining[process["pid"]] > 0
            )

            # Record the idle period.
            gantt.append(
                ("Idle", current_time, next_arrival)
            )

            current_time = next_arrival
            continue

        # Choose:
        # 1. Smallest remaining time
        # 2. Earlier arrival
        # 3. Lower PID
        selected = min(
            available,
            key=lambda process: (
                remaining[process["pid"]],
                process["arrival"],
                process["pid"]
            )
        )

        pid = selected["pid"]

        # Run for one time unit.
        start = current_time
        current_time += 1
        remaining[pid] -= 1

        # Merge consecutive blocks of the same process.
        if (
            gantt
            and gantt[-1][0] == pid
            and gantt[-1][2] == start
        ):
            old_pid, old_start, old_end = gantt[-1]
            gantt[-1] = (
                old_pid,
                old_start,
                current_time
            )
        else:
            gantt.append(
                (pid, start, current_time)
            )

        # If process has finished, record completion.
        if remaining[pid] == 0:
            completion_times[pid] = current_time
            completed += 1

    # Build final results in original input order.
    results = []

    for process in process_list:
        pid = process["pid"]
        completion = completion_times[pid]

        turnaround = completion - process["arrival"]
        waiting = turnaround - process["burst"]

        results.append({
            "pid": pid,
            "arrival": process["arrival"],
            "burst": process["burst"],
            "completion": completion,
            "turnaround": turnaround,
            "waiting": waiting
        })

    return results, gantt