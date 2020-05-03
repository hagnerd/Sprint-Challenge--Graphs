"""
Represents a room in the maze
"""

class Room:
    """
    Represents a room within the maze.
    """
    def __init__(self, name, description, room_id=0, coords=(None, None)):
        self.id = room_id
        self.name = name
        self.description = description
        self.neighbors = {'n': None, 's': None, 'e': None, 'w': None}
        self.x = coords[0]
        self.y = coords[1]

    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"
    def print_room_description(self):
        """
        Prints the room description
        """
        print(str(self))
    def get_exits(self):
        """
        Finds all exits that are available for the room
        """
        exits = []
        possible_neighbors = ['n', 's', 'e', 'w']

        for direction in possible_neighbors:
            if self.neighbors[direction] is not None:
                exits.append(direction)

        return exits

    def get_exits_dict(self):
        """
        Returns a dictionary of only valid exits
        """
        exits = self.get_exits()
        exits_dict = {}

        for direction in exits:
            exits_dict[direction] = None

        return exits_dict

    def get_exits_string(self):
        """
        Returns a print friendly string of the exits
        """
        return f"Exits: [{', '.join(self.get_exits())}]"

    @staticmethod
    def get_opposite(direction):
        """
        Static method that gets the opposite of a given direction
        """
        if direction == 'n':
            return 's'

        if direction == 's':
            return 'n'

        if direction == 'e':
            return 'w'

        if direction == 'w':
            return 'e'

        return None

    def connect_rooms(self, direction, connecting_room):
        """
        Connects the rooms
        """

        if direction not in ['n', 's', 'e', 'w']:
            print("INVALID ROOM CONNECTION")
            return

        self.neighbors[direction] = connecting_room
        connecting_room.neighbors[Room.get_opposite(direction)] = self

    def get_room_in_direction(self, direction):
        """
        Gets the room in a given direction
        """
        if direction not in ['n', 's', 'e', 'w']:
            return None

        return self.neighbors[direction]

    def get_coords(self):
        """
        Gets the coordinates for a given room
        """
        return [self.x, self.y]

    def has_neighbor(self, direction):
        """
        Checks whether the direction given is a valid neighbor
        """
        exits = self.get_exits()

        return direction in exits
