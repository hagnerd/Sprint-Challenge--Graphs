"""
The player in the maze
"""

from room import Room
from stack import Stack

class Player:
    """
    Represents the player
    """
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.visited = {}

        # Visit the room that you are starting in
        self.visit_room()

    def travel(self, direction, show_rooms=False):
        """
        Allows the player to travel in the given direction if the direction is
        valid
        """
        prev_room = self.current_room
        next_room = self.current_room.get_room_in_direction(direction)

        worked = True

        if next_room is not None:
            self.current_room = next_room
            self.visit_room(prev_room, direction)
            if show_rooms:
                next_room.print_room_description()
        else:
            print("You cannot move in that direction.")
            worked = False

        return worked

    def visit_room(self, prev_room=None, direction=None):
        """
        Adds the current room to the visited dictionary
        """
        if not self.has_visited(self.current_room.id):
            self.visited[self.current_room.id] = self.current_room.get_exits_dict()

        if prev_room is not None and direction is not None:
            self.visited[self.current_room.id][Room.get_opposite(direction)] = prev_room.id
            self.visited[prev_room.id][direction] = self.current_room.id

    def walk_path(self):
        """
        Walks the path until it has traversed every possible neighbor
        """
        traversal = Stack()
        path = []
        while not self.has_walked_all_paths():
            while self.has_visited_all_neighbors():
                direction = traversal.pop()
                self.travel(Room.get_opposite(direction))
                path.append(Room.get_opposite(direction))

            if self.current_room.has_neighbor('n') and not self.has_visited_neighbor('n'):
                self.travel('n')
                traversal.push('n')
                path.append('n')

            elif self.current_room.has_neighbor('e') and not self.has_visited_neighbor('e'):
                self.travel('e')
                traversal.push('e')
                path.append('e')

            elif self.current_room.has_neighbor('s') and not self.has_visited_neighbor('s'):
                self.travel('s')
                traversal.push('s')
                path.append('s')

            elif self.current_room.has_neighbor('w') and not self.has_visited_neighbor('w'):
                self.travel('w')
                traversal.push('w')
                path.append('w')

        return path

    def has_walked_all_paths(self):
        """
        Checks whether the player has visited all neighbors of all visited rooms
        to determine whether the entire walkable map has been traversed
        """
        visited_all = True
        for room in self.visited:
            for neighbor in self.visited[room]:
                if self.visited[room][neighbor] is None:
                    visited_all = False

        return visited_all

    def has_visited_all_neighbors(self):
        """
        Checks whether the player has visited all neighbors of the current room
        to determine whether they should start backtracking
        """
        room = self.visited[self.current_room.id]
        visited_all = True

        for neighbor in room:
            if room[neighbor] is None:
                visited_all = False

        return visited_all

    def has_visited(self, room_id):
        """
        Determines if the user has visited the given room
        """
        return room_id in self.visited

    def has_visited_neighbor(self, direction):
        """
        Determines if the user has visited the given neighbor of the current
        room
        """
        return self.visited[self.current_room.id][direction] is not None
