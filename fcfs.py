"""
First Come First Serve (FCFS) Scheduling Algorithm
"""


def fcfs(processes):
    """
    Perform FCFS scheduling.

    Returns:
        results: List of process scheduling results
        gantt: Gantt chart as (pid, start, end) tuples
    """

    # Make a copy so the original process list is not changed
    process_list = processes.copy()

    # Sort by arrival time, then by PID
    process_list.sort(
        key=lambda p: (p["arrival"], p["pid"])
    )

    results = []
    gantt = []

    current_time = 0

    for process in process_list:

        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        # If CPU is idle, add an Idle period
        if current_time < arrival:
            gantt.append(
                ("Idle", current_time, arrival)
            )
            current_time = arrival

        # Process starts
        start_time = current_time

        # Process completes
        completion = start_time + burst

        # Calculate turnaround time
        turnaround = completion - arrival

        # Calculate waiting time
        waiting = turnaround - burst

        # Add process to Gantt chart
        gantt.append(
            (pid, start_time, completion)
        )

        # Store result
        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "completion": completion,
            "turnaround": turnaround,
            "waiting": waiting
        })

        # Move current time forward
        current_time = completion

    return results, gantt
