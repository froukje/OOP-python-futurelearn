from room import Room
from item import Item
from character import Enemy

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

dave = Enemy("Dave", "A smelly zombie!")
dave.set_conversation("Ahhh...I will eat you!")
dave.set_weakness("cheese")


# put dave into the dining hall
dining_hall.set_character(dave)

current_room = kitchen

# items
old_sward = Item("old Sward")
shield = Item("Shield")
wand = Item("wand")
book = Item("Book")

# link items
dining_hall.link_item(old_sward)
kitchen.link_item(shield)

# set description of items
old_sward.set_description("A stump, rusty sward - let's hope you won't need it.")
shield.set_description("A heavy shield good to defend, but heavy to carry.")
wand.set_description("Wow - now you can do some magic!")
book.set_description("A heavy book full of wisdom.")

old_sward.describe()

while True:
    print("\n")
    current_room.get_details() 

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
 
    command = input("> ")
    current_room = current_room.move(command)
    if command in ["exit", "quit"]:
        break
