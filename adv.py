"""
The main file for the maze traversal program
"""

from ast import literal_eval
from player import Player
from world import World


# Load world
WORLD = World()


# You may uncomment the smaller graphs for development and testing purposes.
# MAP_FILE = "maps/test_line.txt"
# MAP_FILE = "maps/test_cross.txt"
# MAP_FILE = "maps/test_loop.txt"
# MAP_FILE = "maps/test_loop_fork.txt"
MAP_FILE = "maps/main_maze.txt"

# Loads the map into a dictionary
ROOM_GRAPH = literal_eval(open(MAP_FILE, "r").read())
WORLD.load_graph(ROOM_GRAPH)

# Print an ASCII map
WORLD.print_rooms()

PLAYER = Player(WORLD.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
TRAVERSAL_PATH = PLAYER.walk_path()


# TRAVERSAL TEST - DO NOT MODIFY
VISITED_ROOMS = set()
PLAYER.current_room = WORLD.starting_room
VISITED_ROOMS.add(PLAYER.current_room)

for move in TRAVERSAL_PATH:
    PLAYER.travel(move)
    VISITED_ROOMS.add(PLAYER.current_room)

if len(VISITED_ROOMS) == len(ROOM_GRAPH):
    print(f"TESTS PASSED: {len(TRAVERSAL_PATH)} moves, {len(VISITED_ROOMS)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(ROOM_GRAPH) - len(VISITED_ROOMS)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
PLAYER.current_room.print_room_description()
while True:
    CMDS = input("-> ").lower().split(" ")
    if CMDS[0] in ["n", "s", "e", "w"]:
        PLAYER.travel(CMDS[0], True)
    elif CMDS[0] == "q":
        break
    else:
        print("I did not understand that command.")
