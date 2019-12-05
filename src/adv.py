from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
from item import Item
item_1 = Item("shovel", "with a wooden handle")
item_2 = Item("flashlight", "with extra batteries")
item_3 = Item("rag", "with oil stains")
item_4 = Item("apple", "that might be poisonous")
item_5 = Item("bird", "to warn off attackers")
room['foyer'].add_item(item_1)
room['foyer'].add_item(item_5)
room['foyer'].add_item(item_4)
room['outside'].add_item(item_2)
room['outside'].add_item(item_3)
print(item_1)

# Make a new player object that is currently in the 'outside' room.
from player import Player
player_1 = Player('Bob', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
choices = ['n', 's', 'e', 'w']
actions = [ 'take', 'drop']
while True: # LOOP

# READ
    print(player_1)
    cmd = input('->').split(" ")
    current_room = player_1.current_room
    if len(cmd) > 1:
        item_interest = cmd[1]
    elif len(cmd) == 1:
        play_direction = cmd[0]
    

    # REPL should accept 'n', 's', 'e', 'w', 'q' commands
    # 'q' to quit
    # EVALUATE
    # print(f"testing again {player_1.current_room.items}") ## previous room's items
    if cmd in choices:
        # do something
        player_1.player_move(play_direction)
        # print(player_1.current_room)
        print(f" testing {player_1.current_room.items}")
    elif cmd in actions:
        if cmd == 'take':
            player_1.add_item(item_interest)
            item_interest.on_take()
        elif cmd == 'drop':
            pass

    elif cmd == 'q':
        # Break out of the loop
        print("Goodbye!")
        break
    else:
        print("Invalid command.")

