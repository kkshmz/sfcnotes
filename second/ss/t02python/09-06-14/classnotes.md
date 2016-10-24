Terminal
```
Artemis:sfc-notes Zenfinitas$ sysctl -n hw.ncpu
4
```
Activity monitor
`4`
System Information
`2`
Hyper-threading

Pipe-Lining

Threads vs Processes

Thread -
Process - within a process you can have Threads

Multicore-processors can run many processes,
what you can see with activity monitors are processes

Thread is factory
<Multi-thread is very simplistic task

Process

ex81.py multiprocessing.Process for multicore processing
intentionally put 5 for range shows more processes than cores.

ex82a.py
threading.Thread for multi threading not multiprocessing

ex82b.py
You want to do the same task with different values of data
for example giving SA tests to grade.
One function to run all different data

ex83.py
About naming, process will automatically name

ex86.py
checking valid state of process, alive or terminated

ex87a.py
managing process

ex89a.py


multi thread to multi processs is changing some names(syntax ) from the slides

Activity monitor
