"""Non-preemptive Priority scheduling (lower number = higher priority)."""


def priority_scheduling(processes):
    """Return (results, gantt) for the given list of process dicts."""
    procs = [dict(p) for p in processes]      # work on a copy
    time = 0
    done = []                                 # finished processes
    gantt = []                                # (pid, start, end)

    while len(done) < len(procs):
        # processes that have arrived and are not finished yet
        ready = [p for p in procs if p["arrival"] <= time and p not in done]

        if not ready:
            # CPU idle: jump to the next arrival
            next_arrival = min(p["arrival"] for p in procs if p not in done)
            gantt.append(("Idle", time, next_arrival))
            time = next_arrival
            continue

        # lowest priority number first; ties -> earlier arrival -> lower PID
        current = min(ready, key=lambda p: (p["priority"], p["arrival"], p["pid"]))

        start = time
        time += current["burst"]
        gantt.append((current["pid"], start, time))

        current["completion"] = time
        current["turnaround"] = current["completion"] - current["arrival"]
        current["waiting"] = current["turnaround"] - current["burst"]
        done.append(current)

    results = sorted(done, key=lambda p: p["pid"])
    return results, gantt