# Scheduling: Introduction

- Scheduling policies -> disciplines.
- Jobs:
  1. Each job runs for the same amount of time.
  2. All jobs arrive at the same time.
  3. Once started, each job runs to completion.
  4. All jobs only use the CPU (i.e., they perform no I/O)
  5. The run-time of each job is known.
- **Scheduling Metric** -> **Turnaraund time**: Time job completes - Time job arrived in system.
- Time job arrived in system = 0, _Turnaround time = Time job completes_.

## FIFO

- Easy to implment.
- **Avarage turnaround time** = Tturnaround of jobs / Njobs.
- **Convoy effect** When the are different lenghts for each process.

## Shortest Job First (SJF)

- The shortest program runs first.
- If the jobs arrived at a certain time, despite the length it organize by arriving order.

## Shortest Time-to-Completion First (STCF)

- If a longer jobs is running when a shortest arrive it changes for the shortest one.

# Response Time

- **Response Time** = Time first run - Time arrival

## Round Robin (RR)

- Runs the job for a time sliece and then runs the next job util it finish all.
- The interrupt time cannot be to short or to long.
- It performs poorly fit turnaround time but it is **fair**.
- **Optimize response time**

# IO

- Overlaps the use of the IO with another job.
