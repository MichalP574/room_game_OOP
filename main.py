from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
ballroom.set_character(catrina)

cheese = Item()
cheese.set_name("cheese")
cheese.set_description("cheese - needed to fight with enemies")
ballroom.room_item = cheese

current_room = kitchen


def print_info(number, noun_singular, noun_plural, sentence_ending):
    noun = noun_plural if number > 1 else noun_singular
    print(f"You have: {number} {noun} {sentence_ending}")


print_info(Room.number_of_rooms, "room", "rooms", "to explore.")

dead = False
backpack = []
enemies = Enemy.number_of_enemies
items_to_find = Item.number_of_items
while not dead:
    print("\n#########################################################################################################")
    print_info(enemies, "enemy", "enemies", "to kill.")
    if enemies == 0:
        print("You won the game!!!")
        break
    print("You are in: ")
    current_room.get_details()
    print_info(items_to_find, "item", "items", "to find.")
    print_info(len(backpack), "item", "items", "in your backpack")
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("\nAvailable commands: north, south, east, west, talk, fight, pick")
    command = input("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack and inhabitant.fight(fight_with):
                # What happens if you win?
                print("Hooray, you won the fight!")
                current_room.set_character(None)
                enemies -= 1
            else:
                # What happens if you lose?
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
                dead = True
        else:
            print("There is no one here to fight with")

    elif command == "pick":
        item_in_current_room = current_room.room_item
        if item_in_current_room is not None:
            backpack.append(item_in_current_room.get_name())
            print(f"{item_in_current_room.get_name().upper()} is in your backpack")
            current_room.room_item = None
            items_to_find -= 1
        else:
            print("There is nothing here to pick up. :(")

RPGInfo.author = "Michal"
RPGInfo.credits()
