# Lock-based Concurrent Data Structures

- Adding locks to data structures makes them thread safe
- Just adding a block may slows the data structure
- **Perfect scaling** -> threads complete as quickly on multiple processors as the single thread does on one
- _Aproximate counter:_ one global counter given many local counters of each thread
- Each thread increments its local counter
- After some time the global counter is syncronized and incremented
- The local counter is reseted to zero
- The smaller the **S** (time) the counter behaves non-scalable
- The bigger the **S** more scalable is the counter but further of the global value might be from actual count
- Small s poor performance
- Big s high performance, global count lags
- **Hand Over Hand Locking** Add a lock per node in the list
- In hash tables use lock per _hash bucket_
