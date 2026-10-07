"""
Round Robin CPU Scheduling Algorithm.

Each process must have:
    pid
    arrival
    burst
    priority

Returns:
    results - list of dictionaries containing:
              pid, arrival, burst, completion,
              turnaround, waiting

    gantt - list of tuples:
            (pid, start, end)

Round Robin uses a fixed time quantum.
"""

from collections import deque


def round_robin(processes, quantum):
    """
    Perform Round Robin CPU scheduling.

    Args:
        processes: List of process dictionaries.
        quantum: Time quantum.

    Returns:
        (results, gantt)
    """

    # Make a copy so the original input list is not modified.
    process_list = [process.copy() for process in processes]

    # Sort by arrival time, then PID.
    process_list.sort(key=lambda p: (p["arrival"], p["pid"]))

    # Store remaining burst time for each process.
    remaining = {
        process["pid"]: process["burst"]
        for process in process_list
    }

    # Store completion times.
    completion = {}

    # Ready queue.
    ready_queue = deque()

    # Gantt chart.
    gantt = []

    # Start the clock at 0.
    time = 0

    # Index of the next process that has not entered the ready queue.
    next_process = 0

    # Continue until all processes are completed.
    while len(completion) < len(process_list):

        # If the ready queue is empty, the CPU is idle.
        if not ready_queue:

            # There are still processes waiting to arrive.
            if next_process < len(process_list):

                next_arrival = process_list[next_process]["arrival"]

                # Record the idle period.
                if time < next_arrival:
                    gantt.append(("Idle", time, next_arrival))
                    time = next_arrival

                # Add all processes that have arrived.
                while (
                    next_process < len(process_list)
                    and process_list[next_process]["arrival"] <= time
                ):
                    ready_queue.append(
                        process_list[next_process]["pid"]
                    )
                    next_process += 1

            continue

        # Take the first process from the ready queue.
        pid = ready_queue.popleft()

        # Run for either the quantum or the remaining burst.
        run_time = min(quantum, remaining[pid])

        start = time
        end = time + run_time

        # Add this execution block to the Gantt chart.
        gantt.append((pid, start, end))

        # Update time and remaining burst.
        time = end
        remaining[pid] -= run_time

        # Add every process that arrived during this time slice
        # before putting the preempted process back into the queue.
        while (
            next_process < len(process_list)
            and process_list[next_process]["arrival"] <= time
        ):
            ready_queue.append(
                process_list[next_process]["pid"]
            )
            next_process += 1

        # If the process has finished, record its completion time.
        if remaining[pid] == 0:
            completion[pid] = time

        # Otherwise, put the process at the back of the ready queue.
        else:
            ready_queue.append(pid)

    # Create the final results.
    results = []

    for process in process_list:

        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        comp = completion[pid]

        # Required formulas.
        turnaround = comp - arrival
        waiting = turnaround - burst

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "completion": comp,
            "turnaround": turnaround,
            "waiting": waiting
        })

    return results, gantt