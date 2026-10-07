# CPU_Scheduling

# CPU Scheduling Algorithm Simulator

## 1. Project Title

**CPU Scheduling Algorithm Simulator**

A Python-based simulator that implements and compares different CPU scheduling algorithms using process scheduling data, Gantt charts, and performance metrics.

---

## 2. Team Members

| Sl. No. | Team Member | Contribution |
|---|---|---|
| 1 | Elakkya A.S. | Main simulator, input handling, FCFS, project integration |
| 2 | Ganashree C.A. | SJF, SRTF, test cases and testing |
| 3 | Gayana Nataraj | Round Robin scheduling and testing |
| 4 | Greeshma V. | Priority scheduling, output functions and final verification |

---

## 3. Problem Statement

CPU scheduling is an important function of an operating system that determines which process should be executed by the CPU and in what order.

Different CPU scheduling algorithms can produce different waiting times, turnaround times, and completion times. Comparing these algorithms manually can be difficult.

Therefore, this project develops a CPU Scheduling Algorithm Simulator that accepts process information, simulates different scheduling algorithms, generates Gantt charts, and calculates important scheduling performance measures.

---

## 4. Project Objective

The main objectives of this project are:

- To understand the working of CPU scheduling algorithms.
- To implement different CPU scheduling algorithms using Python.
- To simulate the execution order of processes.
- To generate Gantt charts.
- To calculate completion time, turnaround time, and waiting time.
- To calculate average waiting time and average turnaround time.
- To compare the performance of different scheduling algorithms.
- To handle different process arrival times and CPU idle periods.
- To test the correctness of the implemented algorithms.

---

## 5. Algorithms Implemented

### 5.1 FCFS - First Come First Serve

FCFS schedules processes according to their arrival order. The process that arrives first is executed first.

### 5.2 SJF - Shortest Job First

SJF selects the process with the smallest burst time among the processes that have already arrived.

SJF is implemented as a non-preemptive scheduling algorithm.

### 5.3 Round Robin

Round Robin gives each process a fixed amount of CPU time called a time quantum.

If a process does not finish within its time quantum, it is moved to the end of the ready queue.

### 5.4 Priority Scheduling

Priority Scheduling selects a process based on its priority.

In this project, a smaller priority number represents a higher priority.

### 5.5 SRTF - Shortest Remaining Time First

SRTF is the preemptive version of SJF.

At each time unit, the process with the smallest remaining burst time is selected for execution.

SRTF is included as an additional scheduling algorithm in this project.

---

## 6. Features

The CPU Scheduling Algorithm Simulator provides the following features:

- Accepts process information as input.
- Supports Process ID (PID).
- Supports arrival time.
- Supports burst time.
- Supports process priority.
- Supports time quantum for Round Robin.
- Implements FCFS scheduling.
- Implements SJF scheduling.
- Implements Round Robin scheduling.
- Implements Priority Scheduling.
- Implements SRTF scheduling.
- Handles CPU idle time.
- Handles scheduling tie-breaking.
- Generates Gantt charts.
- Calculates completion time.
- Calculates turnaround time.
- Calculates waiting time.
- Calculates average waiting time.
- Calculates average turnaround time.
- Allows comparison between scheduling algorithms.

---

## 7. Technology Stack

### Programming Language

- Python

### Libraries

- Matplotlib

### Development Environment

- Visual Studio Code

### Version Control

- Git
- GitHub

### Testing

- Python test files

---

## 8. Project Structure

```text
CPU_Scheduling/
│
├── scheduler.py
├── fcfs.py
├── sjf.py
├── rr.py
├── priority.py
├── srtf.py
├── output.py
├── requirements.txt
├── README.md
├── .gitignore
├── test_cases.txt
│
└── tests/
    ├── test_sjf.py
    └── test_srtf.py

### File Description

| File | Purpose |
|---|---|
| `scheduler.py` | Main simulator and input handling |
| `fcfs.py` | FCFS scheduling algorithm |
| `sjf.py` | Non-preemptive SJF scheduling algorithm |
| `rr.py` | Round Robin scheduling algorithm |
| `priority.py` | Priority scheduling algorithm |
| `srtf.py` | SRTF scheduling algorithm |
| `output.py` | Displays scheduling results and output |
| `requirements.txt` | Required Python libraries |
| `test_cases.txt` | Test cases and expected results |
| `tests/test_sjf.py` | Tests SJF implementation |
| `tests/test_srtf.py` | Tests SRTF implementation |
| `.gitignore` | Files ignored by Git |
| `README.md` | Project documentation |

---

## 9. Input Format

The simulator accepts the following information for each process:

| Input | Description |
|---|---|
| PID | Unique Process ID |
| Arrival Time | Time at which the process arrives |
| Burst Time | CPU time required by the process |
| Priority | Priority assigned to the process |
| Time Quantum | Time limit used by Round Robin |

### Example Input

```text
PID    Arrival Time    Burst Time    Priority

P1     0               5             2
P2     1               3             1
P3     2               8             3
P4     4               2             2
P5     6               4             1

---

## 10. How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/ElakkyaAS/CPU_Scheduling.git

## 11. Output

The simulator produces the following scheduling results:

- Gantt chart
- Process execution order
- Completion time
- Turnaround time
- Waiting time
- Average waiting time
- Average turnaround time

### Example Gantt Chart

```text
| P1 | P2 | P3 | P4 |
0    5    8    16   18

If the CPU is idle before the first process arrives, the idle period is also displayed.

| Idle | P1 | P2 |
0      2    5    10
Example Result
PID    Completion    Turnaround    Waiting

P1     5              5             0
P2     8              7             4
P3     16             14            6
P4     18             14            12

12. Scheduling Formulas

The simulator uses the following standard CPU scheduling formulas.

Completion Time

Completion Time is the time at which a process finishes execution.

Turnaround Time
Turnaround Time = Completion Time - Arrival Time
Waiting Time
Waiting Time = Turnaround Time - Burst Time
Average Waiting Time
Average Waiting Time = Total Waiting Time / Number of Processes
Average Turnaround Time
Average Turnaround Time = Total Turnaround Time / Number of Processes
13. Tie-Breaking Rules

When multiple processes have the same scheduling value, the simulator follows consistent tie-breaking rules.

The order of consideration is:

Scheduling value.
Earlier arrival time.
Lower Process ID (PID).
SJF

The process with the smallest burst time is selected.

If burst times are equal:

Earlier Arrival Time -> Lower PID
SRTF

The process with the smallest remaining burst time is selected.

If remaining times are equal:

Earlier Arrival Time -> Lower PID
Priority Scheduling

A smaller priority number represents a higher priority.

Priority 1 > Priority 2 > Priority 3
14. Testing

Testing is performed to verify that the scheduling algorithms produce the expected results.

Test Case 1 - Normal Case

This test case contains processes with different arrival times and burst times.

It verifies normal scheduling behavior.

Test Case 2 - Same Arrival Time and Tie-Breaking

This test case contains processes arriving at the same time.

It verifies:

Equal arrival times.
Equal burst times.
PID-based tie-breaking.
Test Case 3 - Initial CPU Idle Time

This test case contains processes whose first arrival time is greater than zero.

It verifies that the simulator correctly handles the CPU idle period before the first process arrives.

SJF Testing

The SJF implementation is tested using Python test cases to verify:

Correct process selection.
Correct Gantt chart.
Completion time.
Turnaround time.
Waiting time.
CPU idle handling.
SRTF Testing

The SRTF implementation is tested using processes with different arrival and burst times.

It verifies:

Preemption.
Remaining burst time.
Correct process selection.
Gantt chart generation.
Completion time.
Turnaround time.
Waiting time.

15. Team Contributions
Elakkya A.S.
Developed the main simulator structure.
Worked on input handling.
Implemented FCFS scheduling.
Worked on project integration.

Ganashree C.A.
Implemented non-preemptive SJF.
Implemented SRTF as an additional scheduling algorithm.
Created scheduling test cases.
Tested SJF and SRTF implementations.

Gayana Nataraj
Implemented Round Robin scheduling.
Worked on Round Robin testing.

Greeshma V.
Implemented Priority Scheduling.
Worked on output functions.
Performed final testing and verification.

16. Future Scope

The project can be further improved by adding:

Graphical User Interface (GUI).
Interactive Gantt charts.
Performance comparison graphs.
Additional CPU scheduling algorithms.
Exporting results to CSV or PDF.
Support for larger numbers of processes.
Improved visualization of scheduling performance.
Interactive process input forms.
Better comparison of algorithm performance.

17. Conclusion

The CPU Scheduling Algorithm Simulator provides a simple and practical way to understand and compare different CPU scheduling algorithms.

The simulator accepts process information and applies different scheduling techniques to determine the execution order of processes.

It generates Gantt charts and calculates completion time, turnaround time, waiting time, average waiting time, and average turnaround time.

The project demonstrates the working and performance differences of FCFS, SJF, Round Robin, Priority Scheduling, and SRTF algorithms.

The project also demonstrates software development practices such as modular programming, testing, Git version control, and GitHub-based team collaboration.

18. Academic Project

This project is developed as part of an academic activity to understand CPU scheduling concepts and their implementation.

The project provides practical experience in:

Operating system concepts.
CPU scheduling algorithms.
Python programming.
Algorithm testing.
Git and GitHub collaboration.
Team-based software development.

This project is intended for educational purposes.
