# I/O Devices

- **Internal structure**
  - Status: Tells the current state of the device
  - Command: Tell the device to perform a certain task
  - Data: Passed data to the device, or get data from it
- **Protocol**
  1. OS waits for the device to be ready - **polling**
  1. OS sends data - **programmed I/O**
  1. OS writes a command (this tells the device that the data is ready)
  1. OS waits for the device to finish
- Just _polling_ is a waits of CPU time
- It will be better to switch toa nother process instead
- Put the process to sleep and **interrupt** when the device is ready
- **Interrupt Service Routine (ISR)** ~ Interrupt handler
- Interrupts are not always the solution, if processes end quickly the using interrupts will slow down the CPU
- In network is wors to use interrupts
- Many packets arriving will generate a **livelock**
- **Coalescing** -> Waiting some time before generating the interrupt so many interrupts may be aligned to one
- **Direct Memory Access (DMA)** -> Orchestrate transfers between devices without much CPU intervention
- The OS tells the DMA where the data is located, how much data to copy, and wich device to send it
- When the DMA is completed it arise an interruption so the OS knows the transfer is completed
- **Explicit IO instructions** -> The oldest method to comunicate to a IO device
- **Memory Mapped IO** -> The hardware makes device registers available as if they wheere memory locations
- The **device drivers** works as an interface, the OS just send or get data from the device, the driver translate does instructions to the specific device
