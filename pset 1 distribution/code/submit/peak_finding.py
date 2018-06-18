from __future__ import division
from operator import itemgetter
import math

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
        self.queried_indices= [0, n-1]
        self.count=0
        self.counter=0
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################
        
        # handle a queried cell
        if i in self.current_board and self.current_board[i]!= -1:
            return self.current_board[i]

        self.counter+=1
        if self.counter < math.log(self.n, 2)-1:
            # handle board of size 1
            if self.n == 1:
                self.current_board[i] = self.n
                return self.current_board[i]

            # handle an unqueried cell
            else:
                
                #1. Find where i is 
                rb_index = [val for val in self.queried_indices if i<= val][0]
                qi_index = self.queried_indices.index(rb_index)#
                lb_index = self.queried_indices[qi_index - 1]

                if (i==0):
                    lb_index= rb_index
                    rb_index= self.queried_indices[qi_index + 1]

                #2. Keep track of queried_indices
                if (i!=0 and i!=self.n-1):
                    self.queried_indices.insert(qi_index,i)

                #3. Give i a valid value
                if (self.max_chunk[0] <= i and i <= self.max_chunk[1]): # i is in max_chunk

                    #update max_chunk
                    if (i-self.max_chunk[0] >= self.max_chunk[1]-i):
                        self.max_chunk = [self.max_chunk[0], i]
                    else:
                        self.max_chunk = [i,self.max_chunk[1]]
                        
                    self.count+=1
                    self.current_board[i] = self.count*self.n
                    
                else: # i is not in the max_chunk
                    if rb_index not in self.current_board:
                        self.current_board[rb_index] = -1
                    if lb_index not in self.current_board:
                        self.current_board[lb_index] = -1
                    comp = max(self.current_board[rb_index],self.current_board[lb_index])
                    if comp == self.current_board[rb_index]:
                        self.current_board[i]= comp - abs(rb_index-i)
                    else:
                        self.current_board[i]= comp - abs(lb_index -i)
          
                return self.current_board[i]
        else:
            self.current_board[i]= 1
            return self.current_board[i]

        ###################### End Student code  #######################

