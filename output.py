"""Output helpers: result tables, Gantt chart, comparison and best algorithm."""
import matplotlib.pyplot as plt


def averages(results):
    """Return (average waiting time, average turnaround time)."""
    n = len(results)
    avg_wt = sum(r["waiting"] for r in results) / n
    avg_tat = sum(r["turnaround"] for r in results) / n
    return avg_wt, avg_tat


def print_results(name, results):
    """Print the per-process table and averages for one algorithm."""
    print(f"\n=== {name} ===")
    print(f"{'PID':<6}{'Arrival':<9}{'Burst':<8}{'Completion':<12}{'Turnaround':<12}{'Waiting':<8}")
    for r in results:
        print(f"{r['pid']:<6}{r['arrival']:<9}{r['burst']:<8}"
              f"{r['completion']:<12}{r['turnaround']:<12}{r['waiting']:<8}")
    avg_wt, avg_tat = averages(results)
    print(f"Average Waiting Time    : {avg_wt:.2f}")
    print(f"Average Turnaround Time : {avg_tat:.2f}")


def plot_gantt(all_gantts):
    """Draw one Gantt chart per algorithm. all_gantts = {name: gantt_list}."""
    pids = sorted({pid for g in all_gantts.values() for pid, _, _ in g if pid != "Idle"})
    colors = {pid: plt.cm.tab10(i % 10) for i, pid in enumerate(pids)}
    colors["Idle"] = "lightgrey"

    # constrained_layout re-spaces the charts to fit any window size
    fig, axes = plt.subplots(len(all_gantts), 1,
                             figsize=(10, 1.8 * len(all_gantts)),
                             squeeze=False, constrained_layout=True)
    for ax, (name, gantt) in zip(axes[:, 0], all_gantts.items()):
        for pid, start, end in gantt:
            ax.barh(0, end - start, left=start, color=colors[pid], edgecolor="black")
            ax.text((start + end) / 2, 0, pid, ha="center", va="center", fontsize=9)
        ticks = sorted({t for _, s, e in gantt for t in (s, e)})
        ax.set_xticks(ticks)
        ax.set_yticks([])
        ax.set_title(name, loc="center", fontsize=10, fontweight="bold")
    axes[-1, 0].set_xlabel("Time")
    plt.show()


def print_comparison(all_results):
    """Print the comparison table. all_results = {name: results_list}."""
    print("\n=== Algorithm Comparison ===")
    print(f"{'Algorithm':<20}{'Avg Waiting':<14}{'Avg Turnaround':<16}")
    for name, results in all_results.items():
        wt, tat = averages(results)
        print(f"{name:<20}{wt:<14.2f}{tat:<16.2f}")


def best_algorithm(all_results):
    """Lowest average waiting time wins; ties -> lower average turnaround."""
    best = min(all_results, key=lambda n: averages(all_results[n]))
    wt, tat = averages(all_results[best])
    print(f"\nBest algorithm for this input: {best} "
          f"(Avg WT = {wt:.2f}, Avg TAT = {tat:.2f})")
    return best