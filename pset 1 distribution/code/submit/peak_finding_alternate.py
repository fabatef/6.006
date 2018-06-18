from __future__ import division
from operator import itemgetter

class AdversarialGame(object):
    """
    Represents an instance of the 1D peak-finding game.

    Args:
        n (int): the number of cells in the array. n is guaranteed to be a positive integer.
    """
    def __init__(self, n):
        self.n = n
        ###################### Begin student code ######################
        self.current_board = dict()
        self.max_chunk=[0, n-1]
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################

        if i > self.max_chunk[1]:
            return self.n-i
        if i < self.max_chunk[0]:
            return i+1
            
        if (self.max_chunk[0] <= i and i <= self.max_chunk[1]): # i is in max_chunk

            #update max_chunk
            if (i-self.max_chunk[0] > self.max_chunk[1]-i):
                self.max_chunk = [self.max_chunk[0], i-1]
                
            else:
                self.max_chunk = [i+1,self.max_chunk[1]]
                
        if i > self.max_chunk[1]:
            return self.n-i
        else:
            return i+1

        ###################### End Student code  #######################
##ordex= AdversarialGame(10)
##ordex.query(5)
##ordex.query(0)
##ordex.query(3)
##ordex.query(4)
##ordex.query(2)
##ordex.query(1)
##ordex.query(9)
##ordex.query(7)
##ordex.query(8)
      

