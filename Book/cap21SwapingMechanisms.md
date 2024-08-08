# Beyond Physical Memory: Mechanisms

- The OS needs to store parts of the memory that are in no big demand
- **Hard Disk Drive** slow but big
- **Swap** gives the processes the illusion of large virtual memory
- **Swap Space** -> space for moving pages
- If we have a _TLB miss_ the systems search for the PTE
- Maybe the page is _not present_, because of this exist the **presennt bit**
  - 1 -> present in memory
  - 0 -> page in disk
- Accesing a page that is not in physical memory in a **page fault**
- If page fault then execute **page-fault handler**
- The software _always_ manage page faults
- steps if **page fault**
  1. Looks in the PTE for PFN address
  1. Issue the request to disk to fetch
  1. When I/O completes update page table and mark as present
  1. Update the PFN
  1. Retry the instruction
- After thoes stepts may be a TLB miss
- Because it has I/O it slows the execution
- The **page-replacement policy** to replace another page
- **High watermark** -> When pages >= HW
- **Low watermark** -> When pages < LW => Free memory, until pages >= HW
- **Swap deamon** or **page deamon**
