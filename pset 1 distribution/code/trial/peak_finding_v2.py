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
        self.current_board = [-1]*n
        self.count=0
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################
        
        if self.current_board[i] != -1:
            return self.current_board[i]

        else:           
            
            #Find indices of queried cells
            queried_indices= [w for w,j in enumerate(self.current_board) if j != -1]
            l = [0]
            r = [self.n-1]
            if (0 not in queried_indices):
                l.extend(queried_indices)
                queried_indices= l
            if ((self.n-1) not in queried_indices):
                queried_indices.append(self.n-1)

            #Find size of max chunk
            max_chunk = max([b-a for a, b in zip(queried_indices[:-1], queried_indices[1:])])
            print (max_chunk)
            
            #where is i
            qi_index, lb_index= next((n,m) for (n,m) in enumerate(queried_indices) if i>=m)
            rb_index = queried_indices[qi_index + 1]


            if (rb_index - lb_index) == max_chunk: # i is in max_chunk
                self.count+=1
                print (self.count)
                self.current_board[i] = self.count*self.n
                
            else: # i is not in the max_chunk
                comp = max(self.current_board[rb_index],self.current_board[lb_index])
                if comp == self.current_board[rb_index]:
                    self.current_board[i]= comp - abs(rb_index-i)
                else:
                    self.current_board[i]= comp - abs(lb_index -i)

            print (self.current_board)      
            return self.current_board[i]

        ###################### End Student code  #######################

ordex= AdversarialGame(10)
ordex.query(5)
ordex.query(0)
ordex.query(3)
ordex.query(4)
ordex.query(2)
ordex.query(1)
ordex.query(9)
ordex.query(7)
ordex.query(8)
ordex.query(6)
