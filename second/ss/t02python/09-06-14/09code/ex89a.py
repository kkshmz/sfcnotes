#Demonstrate  that an object can be used (past examples are functions)
#Demonstrate special method  run (the process will look for it first inside the function)


import multiprocessing
import logging
import time

class Worker(multiprocessing.Process):
  def run(self):
    print 'In %s'%self.name
    return

if __name__ == '__main__':
  multiprocessing.log_to_stderr(logging.INFO)
  jobs = []
  for i in range(5):
    p = Worker()
    jobs.append(p)
    p.start()
  #for j in jobs:
    #j.join()
