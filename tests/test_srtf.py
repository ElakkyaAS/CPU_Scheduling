import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from srtf import srtf

# Test case designed to show SRTF preemption
processes = [
    {"pid": "P1", "arrival": 0, "burst": 8, "priority": 2},
    {"pid": "P2", "arrival": 1, "burst": 4, "priority": 1},
    {"pid": "P3", "arrival": 2, "burst": 2, "priority": 3},
    {"pid": "P4", "arrival": 5, "burst": 3, "priority": 2},
]

results, gantt = srtf(processes)

print("SRTF Gantt Chart:")
print(gantt)

print("\nSRTF Results:")

for result in results:
    print(result)