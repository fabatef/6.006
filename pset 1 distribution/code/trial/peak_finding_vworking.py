from __future__ import division
##from operator import itemgetter
import cProfile

class AdversarialGame(object):
    """
    Represents an instance of the 1D peak-finding game.

    Args:
        n (int): the number of cells in the array. n is guaranteed to be a positive integer.
    """
    def __init__(self, n):
        self.n = n
        ###################### Begin student code ######################
        self.current_board = [-1]*n
        self.max_chunk=[0, n-1]
        self.queried_indices= [0, n-1]
        self.srch_rng_lb= 0
        self.srch_rng_ub= n-1
        self.count=0
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################

        # handle board of size 1
        if self.n == 1:
            self.current_board[i] = self.n
            return self.current_board[i]

        # handle a queried cell
        if self.current_board[i] != -1:
            return self.current_board[i]

        # handle an unqueried cell
        else:           

            #1. Find location and size of max chunk
##            search_in = self.queried_indices[self.queried_indices.index(self.max_chunk[0]): self.queried_indices.index(self.max_chunk[1])+1]
##            interval = [(r-l, l , r) for (l,r) in zip(search_in[:-1], search_in[1:])]
##            max_part = max(interval, key=itemgetter(0))
##            self.max_chunk = [max_part[1] , max_part[2]]

            
            #2. Find where i is 
            rb_index = [val for val in self.queried_indices if i<= val][0]
            qi_index = self.queried_indices.index(rb_index)
            lb_index = self.queried_indices[qi_index - 1]

            if (i==0):
                lb_index= rb_index
                rb_index= self.queried_indices[qi_index + 1]

            #3. Keep track of queried_indices
            if (i!=0 and i!=self.n-1):
                self.queried_indices.insert(qi_index,i)

            #4. Give i a valid value
            if (self.max_chunk[0] <= i and i <= self.max_chunk[1]): # i is in max_chunk
                
                if (i-self.max_chunk[0] >= self.max_chunk[1]-i):
                    self.max_chunk = [self.max_chunk[0], i]
                else:
                    self.max_chunk = [i,self.max_chunk[1]]
                    
                self.count+=1
                self.current_board[i] = self.count*self.n
                
            else: # i is not in the max_chunk
                comp = max(self.current_board[rb_index],self.current_board[lb_index])
                if comp == self.current_board[rb_index]:
                    self.current_board[i]= comp - abs(rb_index-i)
                else:
                    self.current_board[i]= comp - abs(lb_index -i)
      
            return self.current_board[i]

        ###################### End Student code  #######################
ordex= AdversarialGame(100)
cProfile.run('ordex.query(7)')
cProfile.run('ordex.query(71)')
cProfile.run('ordex.query(72)')
cProfile.run('ordex.query(20)')
cProfile.run('ordex.query(30)')
cProfile.run('ordex.query(40)')
cProfile.run('ordex.query(50)')
cProfile.run('ordex.query(90)')
cProfile.run('ordex.query(60)')
cProfile.run('ordex.query(70)')
cProfile.run('ordex.query(80)')
