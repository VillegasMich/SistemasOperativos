import time as tm

# Processes and their burst times
processes = [
    {"id": "P1", "burst": 10, "frun": True},
    {"id": "P2", "burst": 4, "frun": True},
    {"id": "P3", "burst": 6, "frun": True},
    # {"id": "P4", "burst": 3, "frun": True},
    # {"id": "P5", "burst": 1, "frun": True},
    # {"id": "P6", "burst": 8, "frun": True},
]

time_quantum = 2


# Function to simulate round-robin scheduling
def round_robin(processes, time_quantum):
    a_turnaround_time = 0
    np = len(processes)
    a_response_time = 0
    time = 0
    while processes:
        for process in list(processes):
            if process["burst"] > 0:
                run_time = min(time_quantum, process["burst"])
                tm.sleep(run_time)
                process["burst"] -= run_time
                time += run_time
                if process["frun"] == True:
                    print(
                        f"The process {process['id']} response time was: {time - run_time}"
                    )
                    a_response_time += time - run_time
                    process["frun"] = False
                print(f"Process {process['id']} runs from {time - run_time} to {time}")
                if process["burst"] <= 0:
                    turnaround_time = (time - run_time) - process["burst"]
                    print(
                        f"process {process['id']} turnaround time was: {turnaround_time}"
                    )
                    a_turnaround_time += turnaround_time
                    processes.remove(process)
                    print(f"Process {process['id']} finishes at time {time}")
    print(f"The avarage turnaround time was: {a_turnaround_time/np}")
    print(f"The avarage response time was: {a_response_time/np}")


round_robin(processes, time_quantum)
