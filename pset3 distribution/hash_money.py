import sys
import matplotlib.pyplot as plt
import itertools
import string
import numpy as np
import time
import random

######################3.4b,c,d
##dic= {}
##init= sys.getsizeof(dic)
##time_elapsed= []
##for i in range(10**7): 
##    if sys.getsizeof(dic) != init: #detect when the table size changes
##        size = sys.getsizeof(dic)
##        diff = size - init
##        percentage = diff/init # percentage of change from its previous size
##        loadfactor = (i-1)/(init/12.0)  #number of keys in the dictionary/number of entries in the dictionary
##        print (i-1, size, init, percentage, loadfactor ,time_elapsed[i-1], time_elapsed[i-2])
##        init= size
##
##    #time elapsed during insertion
##    start = time.time()
##    dic[i] = 1
##    end= time.time()
##    time_elapsed.append(end - start)
##    
### the table doubles for a large number of insertions without deletions
###load factor for larger insertions is approximately 0.666
##print (time_elapsed[2730] == max(time_elapsed[1300:3000])) # True(i= 2730 was inserted when the load factor was reached)

##########3.4 e
##class C(object):
##    def __init__(self, n):
##        self.hash = random.randint(0, n)
##    def __hash__(self):
##        return self.hash
##
##d = dict()
##n_values= [10**i for i in range(10)]
##insert_times= []
##for n in n_values:
##    start_time = time.time()
##    for i in range(10000):
##        x = C(n)
##        d[x]= random.random()
##    end_time = time.time()
##    time_taken = end_time - start_time # time taken for 10000 insertions for some value of n
##    insert_times.append(time_taken)
##    
####print (insert_times)
##plt.plot(np.log10(n_values), insert_times, 'ro')
##plt.show()

##############3.4f
e={}
class D(object):
    def __init__(self, n):
        self.n = n
##    def __hash__(self):
##        return random.randint(0, self.n)

###inserting a string
e[D("3")]= 1

###finding an object after insertion
x= D(1000)
e[x] = 1
##
##print (id(x))
##print (hash(x))
##print (e[x])

###########3.4g
a= [1,2]
b= [1,2]
y= (1,2)
z= (1,2)
#print (a==b, hash(a)==hash(b))
####print (y==z, hash(y)==hash(z))

################3.4i
result = []
##xl = itertools.permutations('abc')
##print ([i for i in x])
def permutations(string, step = 0):
    # if we've gotten to the end, print the permutation
    if step == len(string):
        result.append ("".join(string))
##        print ("".join(string))
    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)


##permutations('abcdefghij')
##def collision(d):
##    
##    start_time = time.clock()
##    str1= result[len(result)-1]
##    init = bin(hash(str1))[-d:]
##    for perm in result:
##        str2= perm
##        current = bin(hash(perm))[-d:]
##        if current == init:
##            end_time= time.clock()
####            print ('collided')
##            break
##    return (str1, str2, end_time-start_time)
##
##d_vals= [i for i in range(32)]
##collisions_1= []
##for d in d_vals:
##    collisions_1.append(collision(d))
##
##print(collisions_1[0])
##plt.plot(d_vals, [c[2] for c in collisions_1], 'ro')
##plt.show()



def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

d_vals= [i for i in range(1,40)]
collisions= []
encountered= {}
time_max, d_max =0,0
for d in d_vals:
    encountered= {}
    start_time = time.time()
    while True:
        str1= randomword(10)
##        remainder = hash(str1)% (2**d)
        remainder= bin(hash(str1))[-d:]
        if (remainder in encountered) and (str1 != encountered[remainder]):
            end_time= time.time()
            if time_max < end_time-start_time:
                d_max= d
                time_max= end_time-start_time 
            collisions.append((str1, encountered[remainder], end_time-start_time))
            print ((d, str1, encountered[remainder], end_time-start_time))
            break
        encountered[remainder]=str1

print(d_max, time_max )
    
plt.plot(d_vals, [c[2] for c in collisions], 'ro')
plt.show()


                              
        
    
    
        
        
    



    

    




