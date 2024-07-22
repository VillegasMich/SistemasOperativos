# The abstraction: The Process

## HOW TO PROVIDE THE ILLUSION OF MANY CPUS?

- Virtualizing the CPUs, stoping the process and running another. (**time sharing**)
- Mechanisims are the low level machinery.
- Context switch, for stopping a task and running another.
- Time sharing uses space sharing, resources divided.
- **Policies** are algorithms for making some kind of decision.
- Separate high level policies from low level policies to gain _modularity_
- **Create** a new procces to run the program.
- **Destroy** processes forcefully.
- **Wait** for a process to stop running.
- **Miscellaneous Control** for suspending a process.
- **Status** to get info.
- **Lazy** loading of the programs.
- The OS gives memory (stack) to the program execution.
- When the program is ready the OS transfer control of the CPU to the new process.
- Running -> Ready -> Blocked.
- The OS will keep a **process list**.
- More states in other systems like **zombie** and **final**.

## KEY PROCESS TERMS

- Majoy OS abstraction of a running program.
- A process mantains a certain state.
