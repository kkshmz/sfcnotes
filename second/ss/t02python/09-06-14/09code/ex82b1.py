#not using Pool (to be coompared with ex82b2.py)
import random

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
#ends here

#res=[]
if __name__ == '__main__':
    #pool example uses [1000000,2000000,1500000,2500000]
    dat=[1000000,2000000,1500000,2500000]
    res=f(sum(dat)) # sum(dat) is the sum of all 
    print res

    #another variant of this example could use the below:
    #for i in [1000000,2000000,1500000,2500000]:
	#res.append(f(i))
    #print res
