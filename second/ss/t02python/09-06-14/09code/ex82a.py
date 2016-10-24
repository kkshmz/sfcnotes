#Basic example of using threading (not multi processing)
#Note the syntax is very similar. Of course you can have parameter in the function like ex82.py
import threading

def worker():
    """thread worker function"""
    print 'Worker'
    return

#used for tracking down the start
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
#tracking down the start
    threads.append(t)
    t.start()

