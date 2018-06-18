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
def graph(labyrinth):
    adjacency_list= {}
    timestep = 0
    for (room1,room2,typ) in labyrinth.corridors:
        
        adjacency_list[room1] = adjacency_list.get(room1, set())
        adjacency_list[room1].add((room2, typ))
        adjacency_list[room2] = adjacency_list.get(room2, set())
        adjacency_list[room2].add((room1, typ))
    return adjacency_list

def filterInRoom(labyrinth):
    filters = {}
    for (room, typ) in labyrinth.filters:
        filters[room] = filters.get(room, set())
        filters[room].add(typ)
    return filters


def explore_single(labyrinth):
    rooms_dict = graph(labyrinth)
    filters = filterInRoom(labyrinth)
    print(filters)
    start = labyrinth.start
    goal = labyrinth.goal
    steps = 0
    queue = [(start, filters[start], steps)]
    visited = []
    total_filters = set()
    while queue:
        curr = queue.pop(0)
        curr_room = curr[0]
        
        curr_filters = curr[1]
        steps = curr[2]

        next_rooms = rooms_dict[curr_room]
       
        for room in next_rooms:
            
            dest = room[0]
            req_filter = room[1]
            if (dest, curr_filters) not in visited:
                if req_filter in curr_filters:
                    if dest == goal:
                        return steps+1
                    else:
                        total_filters = set([])
                        if dest in filters:
                            filters_in_room = filters[dest]
                            for fil in filters_in_room:
                                total_filters.add(fil)

                        for fil in curr_filters:
                            total_filters.add(fil)

                        queue.append((dest, total_filters, steps+1))
                        visited.append((dest, total_filters))
            
    return None

def explore_multiple(labyrinth, timelimit):
    return None
