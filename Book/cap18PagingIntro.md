# Paging: Introduction

- Chop the memory into _fixed-sized_ pieces
- Physical memory as fixed size slots **pages frames**
- It has great _flexibility_ managing the memory
- _Simplicity_ of free space management
- **Free list** -> A list of free pages
- **Page table** -> Store **address translations** for each page
- **Virtual Page Number** (VPN) -> Space `64 bytes = 2^6 -> 6 bits`
- **Offset** -> Page size 16 bytes -> `2 VPN 4 Offset`
- VA 21 = 010101 -> `page: 01 = 1 and address: 0101 = 5`
- We then find the **Physical frame number** (PFN)
- Then translate to find the correct physical memory slot
- Final address -> `1110101 = 117`
- We store the pages in memory
- **Linear page table** -> The simplest way to manage the page table
- To fetch from memory first is needed to fetch from the page tables
- 2 memory access instead of 1. TO SLOW!
