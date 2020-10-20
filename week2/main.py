from room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

# set descriptions of the rooms
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance.")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# link the rooms
kitchen.link_room(dining_hall, "south")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)
