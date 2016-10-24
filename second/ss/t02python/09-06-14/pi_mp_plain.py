import random
import multiprocessing


#caculate the number of points in the unit circle
#out of n points
def monte_carlo_pi_part(n):

    count = 0
    for i in range(n):
        x=random.random()
        y=random.random()

        # if it is within the unit circle
        if x*x + y*y <= 1:
            count=count+1

    #return
    return count


if __name__=='__main__':
    np = multiprocessing.cpu_count()
    print 'You have {0:1d} CPUs'.format(np)

    # Nummber of points to use for the Pi estimation
    n = 1000000
    # will distribute the points around the process
    # iterable with a list of points to generate in each worker
    # each worker process gets n/np number of points to calculate Pi from
for i in range(n) :
    i = [n]
    res = monte_carlo_pi_part(sum(i))
    print "Estimated value of Pi::", sum(monte_carlo_pi_part)/(n*1.0)*4


#source :https://gist.github.com/amitsaha/2036026
