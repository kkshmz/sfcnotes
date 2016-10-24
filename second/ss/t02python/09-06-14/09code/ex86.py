#Demonstrate 'is alive' usage,to check if a process is still alive

import multiprocessing
import time

def slow_worker():
  print 'Starting worker'
  time.sleep(5)#again this is just to simulate actual process that you would have
  print 'Finished worker'

if __name__ == '__main__':
  p = multiprocessing.Process(target=slow_worker)
  #ctime is just a speficic formatof time
  print time.ctime(),'BEFORE:', p, p.is_alive() # this will show that its NOT alive
  p.start()# It should be alive by now!
  print time.ctime(),'DURING:', p, p.is_alive() #this should show that it is alive!
  time.sleep(2)#the process is 5 second, so terminate it after 2 second (before it finish)
  p.terminate() # terminate the process
  time.sleep(0.001) # it does take time until a process is really terminated hence introduce some delay here to reflect it
  print time.ctime(),'TERMINATED:', p, p.is_alive()
  
