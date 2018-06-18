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
def to_graph(lab):
    Adj= {}
    edges = lab.corridors
    for (u,v,f_type) in edges:
        
        Adj[u] = Adj.get(u, set())
        Adj[u].add((v, f_type))
        Adj[v] = Adj.get(v, set())
        Adj[v].add((u, f_type))
    return Adj

def filter_dict(lab):
    result = {}
    for node, filt in lab.filters:
        result[node] = result.get(node, set())
        result[node].add(filt)
    return result


def explore_single(lab):
    
    rooms_graph= to_graph(lab)
    filters = filter_dict(lab)
    
    start = lab.start
    goal = lab.goal
    time = 0
    queue = [(start, filters[start], time)]
    visited = []
    filters_collected = set()
    
    while queue:
        current = queue.pop(0)
        current_room = current[0]
        
        current_filters = current[1]
        time = current[2]

        neighbors = rooms_graph[current_room]
       
        for room in neighbors: 
            next_room = room[0]
            f_type = room[1]
            if (next_room, current_filters) not in visited:
                if f_type in current_filters:
                    if next_room == goal:
                        return time+1
                    else:
                        filters_collected = set([])
                        if next_room in filters:
                            for filt in filters[next_room] :
                                filters_collected.add(filt)

                        for filt in current_filters:
                            filters_collected.add(filt)

                        queue.append((next_room, filters_collected, time+1))
                        visited.append((next_room, filters_collected))
            
    return None

def explore_multiple(labyrinth, timelimit):
    single_exp = explore_single(labyrinth)
    if (single_exp is None) or (single_exp > timelimit):
        return None
    else:
        return 1
