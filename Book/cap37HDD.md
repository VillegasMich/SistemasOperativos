# Hard Disk Drives

- 512-byte blocks sectors
- Each block can be read or written
- The **address space** of the drive
- Each drive may have one or more **platters**
- Each platters has 2 **surface**
- Data is stored in each surface in concentric circles **track**
- A **disk head** attached to a **disck arm** does the reading a witting of a surface
- **Rotation delay** -> Time of the disk to rotate
- The disk arm is located first in the correct **track** and the search the **sector**
- **Transfer** is the final part where data id eaither read from or written to the surface
- Outer tracks may have more sectors than inner tracks due to geometry
- **Track buffer** -> chache of the HDD

## Disk Scheduling

- Decides the requests and decide wich to run next
- We can make a good guess of how long a job will take
- Follow the SJF
- **SSTF Shortest Seek Time First** -> Picks the request on the nearest track to complete dirst
- It will generate _starvation_
- **Elevaor SCAN / C-SCAN** -> moves back and forth across the disk
- Each pass is called a **sweep**
- **SPTF Shortest Position Time First** ->
