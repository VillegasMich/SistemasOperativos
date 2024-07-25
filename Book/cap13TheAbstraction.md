# The Abstraction: Address Spaces

- Early systems where a set of routines, and one running process
- _Multiprogramming_ -> Multiple process run at a given time
- **Efficiency**

## Time Sharing

- Tired of Batch programming
- **Leave processes in memory while switching between them**
- Easy to use abstraction of the fisical memory so processes don't mess with each others
- **Address Space** -> Running program view of the memory of the system
- Code - Stack - Heap
- **Heap** -> Grows positive (down)
- **Stack** -> Grows negative (up)
- It gives an abstraction of the HW memory to the program.
- **Virtualizing Memory**

## Goals

- **Transparency** -> Implement VM invisible to the running program
- **Efficiency** -> In terms of time and space
- **Protection** -> Protect processes from one another
- **Isolation** -> Each process need to run on it own cocoon
