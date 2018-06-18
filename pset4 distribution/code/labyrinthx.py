from collections import deque
class Labyrinth(object):
    def __init__(self, rooms, corridors, filters, start, goal):
        # rooms is a list of the names of the rooms. Each name is a (short) string.
        # For convenience, we won't give you any room names containing numbers.
        self.rooms = rooms  
        # corridors is a list of tuples (room1, room2, type).
        # type is an integer between 0 and 3 (inclusive).
        # All corridors are bidirectional (i.e. can be traversed in either direction).
        # An explorer cannot traverse a corridor of a certain type without possessing the corresponding filter.
        self.corridors = corridors
        # filters gives the initial locations of the filters as a list of tuples (room, type).
        # There may be multiple filters in a room, but there is only one filter of each type.
        # Each explorer may carry any number of filters on his person.
        self.filters = filters
        # start is the name of the room in which the explorer starts.
        self.start = start
        # goal is the name of the (single) room in which the treasure is located.
        self.goal = goal

# This method should return the minimum number of timesteps required to reach the goal room.
# If it is not possible to reach the goal room, return None.
# As stated in the problem set, at the beginning of each timestep, the explorer may pick up any filter 
# located in the same room, and then traverse at most one corridor (provided he possesses the proper filter).

def to_graph(lab):
    Adj= dict()
    edges= deque(lab.corridors)
    while edges:
        u, v, f_type = edges.popleft()   
        Adj[u]= Adj.get(u,[])
        Adj[v]= Adj.get(v,[],)
        Adj[u].append((v, f_type, 0))
        Adj[v].append((u, f_type, 0))
    return Adj

def filter_dict(lab):
    result = dict()
    for node, filt in lab.filters:
        result[node] = result.get(node, set())
        result[node].add(filt)
    return result

def explore_single(lab):

    start, goal = lab.start, lab.goal
    filters= filter_dict(lab)
    my_filters= set()
    visited = set()
    graph = to_graph(lab)
    time = 0

    
    queue= deque()
    queue.append(start)

    while queue:
        
        u = queue.popleft()
        

        
        if (filters.get(u) != None):
            my_filters |= filters[u]
            current_filters= my_filters.copy()

        
        for n, f_type in graph[u]:

            if ((n, list(current_filters)) not in visited) and (f_type in my_filters):
                visited.append((u, list(current_filters)))

                if n == goal:
                    return time
                queue.append(n)


    return None

# This method should return the minimum number of explorers (working simultaneously) required (for any explorer)
# to reach the goal room within the given timelimit. If no group of explorers is big enough, return None.
def explore_multiple(labyrinth, timelimit):
    return None
    
