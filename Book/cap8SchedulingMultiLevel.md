# Scheduling: The Multi-Level Feedback Queue

- **MLFQ**
- Optimize _turnaround time_, running shortest jobs first.
- Make the system feel responsive to the user.
- Minimize _response time_
- Learns from the past to predict the future.

## RULES (summary)

• **Rule 1:** If Priority(A) > Priority(B), A runs (B doesn’t).

• **Rule 2:** If Priority(A) = Priority(B), A & B run in round-robin fashion using the time slice (quantum length) of the given queue.

• **Rule 3:** When a job enters the system, it is placed at the highest priority (the topmost queue).

• **Rule 4:** Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced (i.e., it moves down one queue).

• **Rule 5:** After some time period S, move all the jobs in the system to the topmost queue.

## BASIC RULES

- Has a number of distinct queues.
- Each queue with a different priority level.
- Which ready job to run at a certain time.

- **Rule 1:** If Priority(A) > Priority(B), A runs (B doesn’t).
- **Rule 2:** If Priority(A) = Priority(B), A & B run in RR.

- _Varies_ the priority of a job based on its _observed behavior_

## CHANGE PRIORITY

- **Jobs allotment** -> Amount of time a job can spent at a given priority.

- **Rule 3:** When a job enters the system, it is placed at the highest priority (the topmost queue).
- **Rule 4a:** If a job uses up its allotment while running, its priority is reduced (i.e., it moves down one queue).
- **Rule 4b:** If a job gives up the CPU (for example, by performing an I/O operation) before the allotment is up, it stays at the same priority level (i.e., its allotment is reset).

- It _assumes_ that is a short job by giving high priority.
- If it is longer the priority decreases.

## PROBLEMS

- If there are to many interactive jobs it will consume the CPU time.
- **Game the scheduler** trick the system to give more resources.

## PRIORITY BOOST

- **Rule 5:** After some time period S, move all the jobs in the system
  to the topmost queue.

- Processes are guaranteed not to _starve_.
- **voo-doo constants** -> variables like S for the OS to work.
- Today values like S are set with machine learning.

## PREVENT GAMING THE SCHEDULER

- **Rule 4:** Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced (i.e., it moves down one queue).
