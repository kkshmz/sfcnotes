#Demonstrate how to activate a log  that capture standard error. This will help in debugging

import multiprocessing
import logging
import sys

def worker():
  print 'Doing some work'
  #sys.stdout.flush()

if __name__ == '__main__':
  multiprocessing.log_to_stderr(logging.INFO) # This line enable logging
  p = multiprocessing.Process(target=worker)
  p.start()

