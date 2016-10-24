#Demonstrate that a name can be assigned to process.Also this example does not use loop like previous examples when creating process.
#System will assign a name for the process if you do not assign one 'Process-3' will be assigned automatically for worker_2)

import multiprocessing
import time

def worker():
  name = multiprocessing.current_process().name
  print name, 'Starting'
  time.sleep(2) #this is used to simulate the actual process that you would run
  print name, 'Exiting'

def my_service():
  name = multiprocessing.current_process().name
  print name, 'Starting'
  time.sleep(3) #this is used to simulate the actual process that you would run
  print name, 'Exiting'

if __name__ == '__main__':
  service = multiprocessing.Process(name='my_service', target=my_service)
  worker_1 = multiprocessing.Process(name='worker 1', target=worker)
# will still get named after running even without name value
  worker_2 = multiprocessing.Process(target=worker)
  worker_1.start()
  worker_2.start()
  service.start()



