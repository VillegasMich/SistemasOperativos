# Processes with their priorities and burst times
processes = [{'id': 'P1', 'priority': 2, 'burst': 10},
             {'id': 'P2', 'priority': 1, 'burst': 4},
             {'id': 'P3', 'priority': 3, 'burst': 6}]

# Function to simulate priority scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: x['priority'])
    time = 0
    for process in processes:
        print(f"Process {process['id']} starts at time {time}")
        time += process['burst']
        print(f"Process {process['id']} finishes at time {time}")

priority_scheduling(processes)

