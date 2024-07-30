import time as tm

# Processes with their arrival and burst times
processes = [
    {"id": "P1", "arrival": 0, "burst": 10},
    {"id": "P2", "arrival": 2, "burst": 4},
    {"id": "P3", "arrival": 4, "burst": 6},
]


# Function to simulate FCFS scheduling
def fcfs(processes):
    a_turnaround_time = 0
    a_response_time = 0
    time = 0
    total_waiting_time = 0
    for process in processes:
        if time < process["arrival"]:
            time = process["arrival"]
        wait_time = time - process["arrival"]
        total_waiting_time += wait_time
        print(f"Process {process['id']} starts at time {time}")
        r_time = time - process["arrival"]
        a_response_time += r_time
        print(f"Process {process['id']} response time was {r_time}")
        # tm.sleep(process["burst"])
        time += process["burst"]
        ta_time = time - process["arrival"]
        a_turnaround_time += ta_time
        print(f"Process {process['id']} turnaround time was {ta_time}")
        print(f"Process {process['id']} finishes at time {time}")
    avg_waiting_time = total_waiting_time / len(processes)
    print(f"The avarage response time was {a_response_time/len(processes)}")
    print(f"The avarage turnaround time was {a_turnaround_time/len(processes)}")
    print(f"Average waiting time: {avg_waiting_time}")


fcfs(processes)
