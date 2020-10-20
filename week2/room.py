class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms: " + repr(self.linked_rooms))

    def get_details(self):
        print("The " + self.get_name())
        print("-"*20)
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction.upper().lower() in self.linked_rooms:
            return self.linked_rooms[direction.upper().lower()]
        elif direction.upper().lower() in ["north", "south", "east", "west"]:
            print("You can't go in this direction")
            return self 
        else:
            print("invalid input")
            return self
