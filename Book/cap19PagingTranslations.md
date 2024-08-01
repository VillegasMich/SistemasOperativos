# Paging: Faster translations (TLBs)

- Regular paging is two slow, One more access to memory
- **Translation-lookaside buffer (TLB)** -> parto of the _MMU_
- HW **cache** of popular virtual-to-physical translations
- The HW first cheks this cache and if it is not there it goes into the list
- Steps:
  1. Extract the VPN
  1. Check TLB for translation of VPN
  1. If `true` then **TLB hit**
  1. Translate
  1. **SUCCESS**
  1. If `false` then **TLB miss**
  1. Search in memory for page tables
  1. Translate
  1. **SUCCESS**
- The TLB stores the entire page!
- TLB **hit rate** -> num-of-hits / num-of-accesses
- We want the highes hit rate possible, nearly _100%_
- **spatial locality** -> elements near each other in space
- The larger the page size then fewer misses
- **Tempora locality** -> quick re-referencing of memory items in time
- When TLB miss enters the OS with a **trap handler**
- **Fuly associative** -> any given translation could be anywhere in the TLB
- `VPN | PFN | other bits`
- Other bits:
  - valid bit
  - protection bit
  - address-space identifier
  - dirty bit
- **TLB contains translations of the current running process**
- **Flush** -> emptying before running the ext process
- We ensures a TLB miss in the new process
- **Address space identifier (ASID)** -> like the PID but for searching in the TLB
- **cache replacement** -> replace one slot, which one?
- **Least-Recently-Used (LRU)** or **Random**
