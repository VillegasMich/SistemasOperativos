# Mechanism: Limited Direct Execution

- The need to share de CPU among different jobs.
- Can be achieved by **time sharing**.
- _Performance_ and _control_ are 2 core items.
- **Get good performance while keeping the CPU control**.
- **Limited Direct Execution** a way to run programs directly on the CPU.
- Create entry process -> run main() -> free memory and remove.

## PROBLEM 1: RESTRICTED OPERATIONS

- Running the process on the CPU is fast but gives access to restricted operations.
- The introduction of the **user mode**.
- Code that runs in user mode is _restricted_ in what it can do.
- In contrast there ins the **kernel mode**.
- Code that runs in this mode have free access to everything.
- When a user mode program wishes to make a restricted action it generate a **system call**.
- **Trap** jump from user to kernel.
- **Return-from-trap** jumpp from kernel back to user.
- Treat the user input with carefull.

## PROBLEM 2: SWITCHING BETWEEN PROCESSES

- There is no way of the CPU to make an action if it is not running.
- **How does the OS regain control of the CPU?**
- Application often gives control when the program does something illegal.
- When the program has an infinite loop the OS takes control.
- **Timer interrupt**, interrupt every so many milliseconds.
- The timer can be stopped.
- **Context switch** when the return-from-trap is executed it return but to the nest process.
