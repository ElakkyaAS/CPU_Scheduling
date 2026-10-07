import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sjf import sjf

# Test case with initial CPU idle time
from sjf import sjf


processes = [
    {"pid": "P1", "arrival": 2, "burst": 3, "priority": 2},
    {"pid": "P2", "arrival": 4, "burst": 5, "priority": 1},
    {"pid": "P3", "arrival": 5, "burst": 2, "priority": 3},
    {"pid": "P4", "arrival": 7, "burst": 4, "priority": 2},
]

results, gantt = sjf(processes)

print("SJF Gantt Chart:")
print(gantt)

print("\nSJF Results:")

for result in results:
    print(result)