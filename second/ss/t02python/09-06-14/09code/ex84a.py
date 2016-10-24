#demonstrate join


import multiprocessing
import time
import sys

def daemon():
    print 'Starting:', multiprocessing.current_process().name
    time.sleep(5)
    print 'Exiting :', multiprocessing.current_process().name

def non_daemon():
    print 'Starting:', multiprocessing.current_process().name
    print 'Exiting :', multiprocessing.current_process().name

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
    
'''''
source: http://pymotw.com/2/multiprocessing/basics.html

To wait until a process has completed its work and exited, use the join() method.
Since the main process waits for the daemon to exit using join(), the "Exiting" message is printed this time.

By default, join() blocks indefinitely. It is also possible to pass a timeout argument
(a float representing the number of seconds to wait for the process to become inactive).
If the process does not complete within the timeout period, join() returns anyway. Example below:
    d.join(1)
    print 'd.is_alive()', d.is_alive()
    n.join()
Since the timeout passed is less than the amount of time the daemon sleeps, the process is still "alive" after join() returns.
'''''
   

