# Locks

- Locks around critical sections to protec
- Let execute single atomic instructions
- **Available** -> Unlock or free
- **Acquired** -> Locked or held
- If the lock is free a thread acquire that lock and prevents others from gettin in
- The mutex does not let another thread to get in (will not return)
- **Mutex** provide **mutual exclusion** btween threads
- Lock properties
  1. mutual exclusion
  1. fairness (don't **starve** other threads)
  1. performace
- **Interrupt disabling**, too much trust, not in multiprocessors
- If a thread try to acces a held lock then just _spins-wait_ (just moves to wait status)
- **test-and-set** (atomic exchange) -> updates the value to new, returns the old value
- **spin locks** don't provide any fairness
- **loaded-linked** and **store-conditional**
  - The thread waits until flag is 0 (not held)
  - Tries to acquire the lock (with store-conditional)
  - Change the flag to 1 (held)
  - Proceed into critical section
- **fetch-and-add** -> increments a value returning the old value
- **ticket-lock** -> uses a ticket and turn variable in combination to build a lock
- When a thread is going to spin it just **yeild the CPU**
- **Deschedules** itself
- We can put to **sleep** the threads
- With the wrong timing a thread may sleep/wait forever
- **two-phase-locks** -> A thread spins for some time, if can't acquire the lock the is put to sleep
