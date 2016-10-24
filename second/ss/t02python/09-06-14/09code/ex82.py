import multiprocessing

# the difference to ex81.py is that this demonstrate that parameter (n ) is passed
# Note how it is passed as args in Process
def worker(num):
   """worker function"""
   print 'Worker:', num
   return

if __name__ == '__main__':
  jobs = []
  for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    #note the format of args (need comma after i) for 2 or more arguments the trailing comma is not required
    jobs.append(p)
    p.start()


