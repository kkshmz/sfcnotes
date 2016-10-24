#Basic examples of using Pool in multiprocessing
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes(assuming number of core=4)
    
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"

#if you don't know the number of cores then you can use np where np = multiprocessing.cpu_count()
