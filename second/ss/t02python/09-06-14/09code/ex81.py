#Basic example of using multi processing
import multiprocessing

def worker():
   """worker function"""
   print 'Worker'
   return

#safe guard for multiprocessing
if __name__ == '__main__':
  jobs = [] # this list has NO function except for tracking down/collecting process object,which could be useful in some cases(for example in ex87.py)
  for i in range(5):
    p = multiprocessing.Process(target=worker)
    jobs.append(p) #here it adds the object created into the list above
    p.start()


