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
        self.max_chunk=[0, n-1]
        self.count=0
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################
##        print ("round ", self.count, "queried= ", i)
##        print (self.current_board)
        if self.n == 1:
            self.current_board[i] = self.n
            return self.current_board[i]
        
        if self.current_board[i] != -1:
            return self.current_board[i]

        else:           
            
            #1. Find indices of queried cells
            queried_indices= [w for w,j in enumerate(self.current_board) if j != -1]
            l = [0]
            r = [self.n-1]
            if (0 not in queried_indices):
                l.extend(queried_indices)
                queried_indices= l
            if ((self.n-1) not in queried_indices):
                queried_indices.append(self.n-1)

            #2. Find size and location of max chunk
            [srch_rng_lb] = [queried_indices.index(z) for z in queried_indices if z == self.max_chunk[0]]
            [srch_rng_ub] = [queried_indices.index(y) for y in queried_indices if y == self.max_chunk[1]]
            search_in = queried_indices[srch_rng_lb: srch_rng_ub+1]
            
            max_c = max([b-a for a, b in zip(search_in[:-1], search_in[1:])])
            (a, b) = next((a, b) for a,b in zip(search_in[:-1], search_in[1:]) if b-a == max_c)
            self.max_chunk = [a, b]

##            print ("current max_chunk: ", self.max_chunk)
            
            #3. Find where i is 
##            print ("queried inices: ", queried_indices)
            qi_index, rb_index= next((ind,val) for (ind,val) in enumerate(queried_indices) if i<=val)
            lb_index = queried_indices[qi_index - 1]
##            print ("i's lb index: ", lb_index, "i's rb index: ", rb_index)
            if (i==0):
                lb_index= rb_index
                rb_index= queried_indices[qi_index + 1]


            #4. Give i a valid value
            if (self.max_chunk[0] <= i and i <= self.max_chunk[1]): # i is in max_chunk
                #print (i, "is in max chunk")
                self.count+=1
                self.current_board[i] = self.count*self.n
                
            else: # i is not in the max_chunk
##                print (i, "is not in max chunk")
                comp = max(self.current_board[rb_index],self.current_board[lb_index])
                if comp == self.current_board[rb_index]:
                    self.current_board[i]= comp - abs(rb_index-i)
                else:
                    self.current_board[i]= comp - abs(lb_index -i)
      
            return self.current_board[i]

        ###################### End Student code  #######################

##ordex= AdversarialGame(1)
##ordex.query(7)
##ordex.query(0)
##ordex.query(0)
##ordex.query(3)
##ordex.query(4)
##ordex.query(5)
##ordex.query(2)
##ordex.query(1)
##ordex.query(9)
##ordex.query(7)
##ordex.query(8)
##ordex.query(6)
##ordex.query(7)
##ordex.query(9)
##ordex.query(1)


