#Demonstrate the the way to terminate process

import multiprocessing
import sys
import time

#these functions are created to simulate the behaviour of different processes woth different type of exitiig characteristics

def exit_error():
  sys.exit(1)

def exit_ok():
  return

def return_value():
  return 1


def terminated(): # this will get terminated below before it finish
  time.sleep(3)

if __name__ == '__main__':
  jobs = [] # this is now useful to trackdown job status

  for f in [exit_error, exit_ok, return_value, terminated]:
    print 'Starting process for', f.func_name # note that you can return func_name here
    j = multiprocessing.Process(target=f, name=f.func_name)#name the process
    jobs.append(j) #put the jobs in a list for tracking purpose ie. exit error would be 1 exit ok would be 2
    j.start()#start the processs

  jobs[-1].terminate() # remember -1 in list means the last element of the list! This meant to run for 3 seconds (longer than others)

  
  for j in jobs:
    print '%s.exitcode = %s' % (j.name, j.exitcode)

 
