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
        self.query_state = [False]*n
        self.current_board = [None]*n
        self.val= 0
        ###################### End Student code  #######################

    def query(self, i):
        """
        Returns the value in the ith cell. 
        The return value must be positive and consistent with previous queries.
        """
        ###################### Begin student code ######################

        #if the ith index has already been queried, return its previous result
        if self.query_state[i] == True:
            return self.current_board[i]


        #if ith index hasn't been queried, and it's not a corner cell
        if self.cell_state[i] == False and (i > 1 and i < n-2) :
             self.query_state[i]= True

             #and one or both its neighbors haven't been queried
            if self.query_state[i+1] == False or self.query_state[i-1] == False:
                self.val+=n 
                self.current_board[i]= self.val
                return self.current_board[i]

            #and both its neighbors have been queried
            if self.query_state[i+1] == True and self.query_state[i-1] == True:
                right= self.current_board[i+1]
                left= self.current_board[i-1]
                #find max of the left and right
                higher = max(left,right)
                
                #if the vicinity is clear, assign the cell higher-1 value
                if (higher==left and self.query_state[i-2]== False) or (higher==right and self.query_state[i+2]== False):
                    self.current_board[i]= higher - 1
                    return self.current_board[i]

                #if not
                else:
                    if (higher == left and left >self.current_board[i-2]) or (higher == right and right >self.current_board[i+2]):
                        self.val+=n
                        self.current_board[i]= self.val
                    else:
                        self.current_board[i]= higher - 1

                    return self.current_board[i]

        #corner cases :/
        else:
            if (i= 0 or i = 1):
                queried = self.query_state.index(True)
                self.current_board[i]= self.current_board[queried] - queried
                self.query_state[i] = True
                return self.current_board[i]
            if (i >= n-2):
                self.val+=n
                self.current_board[i]=self.val
                self.query_state[i] = True
                return self.current_board[i]

    ###################### End Student code  #######################
