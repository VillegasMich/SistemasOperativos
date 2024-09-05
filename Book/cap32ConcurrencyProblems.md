# Concurrency Bugr

## Non deadlock bugs

### Atomicity-Violation Bugs

- Not ensure the atomicity of an instruction
- Solve by using locks, sometims don't

### Order-Violation Bugs

- The desire order between threads are changed
- Solved by using **condition variables**
- Signal the other thread when we want to execute

## Deadlock Bugs

- **Deadlock** -> A thread holding a lock (L1) and waiting for another one (L2)
- The thread 2 is holding the L2 and waiting for L1 to be unlocked
- **Conditions for Deadlock:**
  - Mutual exclusion
  - Hold and wait
  - No preemption
  - Circular wait
- **Prevent circular wait** -> Aquire locks in a certani order always (L1 -> L2)
- In complex scenarios **partial ordering** may be used
- The grabbing of locks to be consider a critical section
- **Prevent no preemption** -> Use things like `trylock()`
- Use things like `compareAndSwap()` to keep something like mutex
-
