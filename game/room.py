class Room():

    number_of_rooms = 0

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.linked_items = []
        self.character = None
        Room.number_of_rooms += 1
        self.item = None

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

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item 

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms: " + repr(self.linked_rooms))

    def get_details(self):
        print("The " + self.get_name())
        print("-"*20)
        self.describe()
        print("-"*20)
        if self.get_item():
            for item in self.linked_items:
                print("In the " + self.get_name() + " is a " + item.get_name())
	
        print("\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction.upper().lower() in self.linked_rooms:
            return self.linked_rooms[direction.upper().lower()]
        elif direction.upper().lower() in ["north", "south", "east", "west"]:
            print("You can't go in this direction")
            return self

    def link_item(self, item_to_link):
        self.linked_items.append(item_to_link)
