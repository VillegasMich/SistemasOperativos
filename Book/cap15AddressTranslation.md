# Mechanism: Address Translation

- **Limited Direct Execution (LDE)** -> Let the program run directly on the HW
- The OS, at **interposing**, gains _control_ and _efficiency_
- **Hardware Based Address Translation**
- the HW transforms each memory access changing the **virtual** address to a **physycal**
- The OS helps the HW to store the information
- Creates the perfect **illusion**

## Dynamic (Hardware-based) Relocation or Base and Bounds

- 2 HW registers, **base** and **bounds** (one pair per CPU)
- When the program starts running the OS decides where to put it, it sets the **base** register to that location
- _physical address = virtual address + base_
- Modify all the addresses and then runs the program
- **bound** register helps with protection
- If the program want to access a 16 KB or higher memory address the CPU woll raise and exception
- **Memory Management Unit** (MMU)
- The OS eill set the values before the program runs

## Operating Systems Issues

- The OS will find the space to run the program
- Search the **free list** to find room for the new process and mark it as used
- When the program finish the OS must clean al the space for another program to use it
- Saves the base and bound on a structure like the PCB
- When the program stops the OS can **change the memory allocation**
- Provides **exception handlers**
