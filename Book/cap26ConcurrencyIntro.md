# Concurrency: An Introduction

- A **thread** is like a proccess but they **share** the address space
- It has its how PC
- Switching bwteen threads in the same processor is necesary a **context switch**
- Save contexts to **Thread Control Block** (TCBs)
- The address space stays the same, we do not save pages.
- There is one stack per thread in the address space
- The use of threads helps with avoiding blocks due to slow I/O operations
- Overlapping of I/O
- We can not say that the first thread will run first
- When 2 threads change a shared variable may generate some **indeterministic** results
- There may be data losses
- **Data race** -> **Critical section** -> a piece of code that accesses a shared variable and must not be concurrently executed by more than one thread
- **Mutual exclusion** -> If a thread is using a critical section another thread will not use it
- **Atomic Instructions** -> One instruction to do everithing we want
