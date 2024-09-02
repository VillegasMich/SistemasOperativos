# Semaphores

- **Semaphore** -> object with integer value we can manipulate
- **sem_wait()** -> decrements the value of the semaphore by one, wait if semaphore is negaive
- **sem_post()** -> increments the value of the semaphore by one, if there is a thread waiting wokes up one
- When a thread tries to access it decrements the semaphore then is put to sleep if there is another thread inside
- **binary semaphore** -> 2 states 0, 1
- **ordering semaphores** -> value: 0, parent sleeps - value: -1, child runs - value: 1

## Bounded Buffer Problem

- With multiple threads (producers and consumers) we face a _race condition_
- We may face ovewitting values
- The consumer holds the mutex and is waiting for the someone to signal full. The producer could signal full but is waiting for the mutex. Thus, the producer and consumer are each stuck waiting for each other

## Reader Write Lock

- Inserting is a critical section, but reading is not
- Ensure a single thread can write
- When a readers aquire the lock it increments the value to track how many readers are
- When the first reader aquire the read lock it will aquire the writer lock semaphore
- There can be many readers at the same time, but only one writter when there are not readers
- The writters may starve waiting

## Dining Philosopher's Problem

- 5 philosophers each with 2 forks on each side in a rounding table
- If all philosophers try to get the for on the left the all be waiting at the end
- **Dijkstra** solves this problem by changing the get fork order from one philosopher

## Thread Throttling

- Control how many threads can execute using a semaphore
- Initialize the semaphore with the maximum threads desire
