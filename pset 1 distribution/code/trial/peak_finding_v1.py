from __future__ import division

class AdversarialGame(object):
    """
    Represents an instance of the 1D peak-finding game.

    Args:
        n (int): the number of cells in the array. n is guaranteed to be a positive integer.
    """
    def __init__(self, n):
        self.n = n
        ###################### Begin student code ######################
        self.current_board = [None]*n
        self.count=0
        self.val= 0
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################
        
        if self.current_board[i] != None:
            return self.current_board[i]

        else:
            self.count+=1
            
            #Find indices of queried cells
            queried_indices= [w for w,j in enumerate(self.current_board) if j != None]

            #board not queried yet
            if not queried_indices:
                self.current_board[i] = n
                return self.current_board[i]
            
            #board queried once
            elif len(queried_indices) == 1:
                if i > queried_indices[0]:
                    self.current_board[i] = self.count*self.n
                else:
                    self.current_board[i] = self.current_board[self.quereid_indices[0]]- self.quereid_indices[0]
                return self.current_board[i]
            
            #multiple queried
            else:
                #Find size of max chunk (add 0 and n-1
                max_chunk = max([b-a for a, b in zip(self.queried_indices[:-1], self.queried_indices[1:])])

                #where is i
                lb_index = next( m for (n,m) in enumerate(queried_indices) if i>m)
                rb_index = queried_indices[lb_index + 1]


                if (rb_val - lb_val) == max_chunk: # i is in max_chunk
                    self.current_board[i] = self.count*self.n
                    
                else: # i is not in the max_chunk
                    comp = max(self.current_board[rb_index],self.current_board[lb_index])
                    if comp == self.current_board[rb_index]:
                        self.current_board[i]= comp - (rb_index - i)
                    else:
                        self.cureent_board[i]= comp - (i - lb_index)
                        
                return self.current_board[i]

        ###################### End Student code  #######################
