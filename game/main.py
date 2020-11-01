from room import Room
from item import Item
from character import Enemy
from character import Character
from character import Friend

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

# set characters
dave = Enemy("Dave", "A smelly zombie!")
dave.set_conversation("Ahhh...I will eat you!")
dave.set_weakness("cheese")

susi = Character("Susi", "A cute little puppy")
susi.set_conversation("Wuff, wuff!")

ricky = Friend("Ricky", "A lovely penguin")
ricky.set_conversation("Hello!")


# put characters into rooms
dining_hall.set_character(dave)
ballroom.set_character(susi)
kitchen.set_character(ricky)

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

loop = True
while True:
    print("\n")
    if loop:
        current_room.get_details() 

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()

    print("What do you want to do? ['talk', 'fight', set enemy to sleep, hug a friend, change the room]\n") 
   
    command = input("> ")
    if command.upper().lower() in current_room.linked_rooms:
        loop = True
        current_room = current_room.move(command)
    elif command.upper().lower() in ['north', 'south', 'east', 'west']:
        loop = False
        current_room = current_room.move(command)
    elif command.upper().lower() =="talk":
        loop = False
        if inhabitant:
            print("Talk to " + inhabitant.name + "!")
            inhabitant.talk()
        else:
            print("Sorry, there is nobody else in the room.")	
    elif command.upper().lower() =="fight" and isinstance(inhabitant, Enemy):
        loop = False
        if inhabitant:
            print("Fight against " + inhabitant.name + "!")
            print("What would you like to fight with?")
            combat = input("[combat item] > ")
            if inhabitant.fight(combat) == False:
                break
        else:
            print("Sorry, there is nobody else in the room.")
    elif command.upper().lower() == 'sleep' and isinstance(inhabitant, Enemy):
        loop = False
        inhabitant.sleep()
    elif command.upper().lower() == "hug" and isinstance(inhabitant, Friend):
        inhabitant.hug()
    elif command in ["exit", "quit"]:
        print("Awww...already leaving?") 
        break
    else:
        print("Invalid input.")
        loop = False	
