#Basic examples of using Pool in multiprocessing
import random
import multiprocessing
from multiprocessing import Pool

#part of monte carlo pi calculation, but don't worry too much about how it works for now
#just note that it will loop n number of time

def f(n):

    count = 0
    for i in range(n):
        x=random.random()
        y=random.random()

        if x*x + y*y <= 1:
            count=count+1

    return count



if __name__ == '__main__':
    np = multiprocessing.cpu_count()
    pool = Pool(np)              # start 4 worker processes(assuming number of core=4)
    print pool.map(f, [1000000,2000000,1500000,2500000])

#if you don't know the number of cores then you can use np where np = multiprocessing.cpu_count()
