from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("rock", "this rock is 5 feet by 5 feet"), Item("hammer", "this rock magically hammer")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("wood", "there are 5 pieces if wood"), Item("chocolate", "this will heal you back to 100 percent")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("knife", "this is a wood knife"), Item("compass", "this well prove you with better directions")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("sword", "this is a golden sword"), Item("gloves", "these gloves will heal all injuries sustained throughout your journey")]),

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


player1 = Player("dylan", room["outside"])
is_playing = True

while is_playing:

    print(player1.current_room_nice_print())
    print(f"\n****Available Items in room listed below ****\n")

    for item in player1.current_room.show_items_in_room():
        print(f"{item}\n")

    desired_request = input('What do you want to do ')
    desired_request_split = desired_request.split(' ')

    if len(desired_request_split) == 1:

        if desired_request.lower() == "n":
            if player1.current_room.n_to:
                player1.current_room = player1.current_room.n_to
            else:
                print("********sorry you hit a wall*********\n*****Below is your current location*****")

        elif desired_request.lower() == "s":
            if player1.current_room.s_to:
                player1.current_room = player1.current_room.s_to
            else:
                print("********sorry you hit a wall*********\n*****Below is your current location*****")

        elif desired_request.lower() == "e":
            if player1.current_room.e_to:
                player1.current_room = player1.current_room.e_to
            else:
                print("********sorry you hit a wall*********\n*****Below is your current location*****")

        elif desired_request.lower() == "w":
            if player1.current_room.w_to:
                player1.current_room = player1.current_room.w_to
            else:
                print("********sorry you hit a wall*********\n*****Below is your current location*****")
        
        elif desired_request.lower() == 'i':
            print("\n*****Items your carrying listed below*****\n")
            for item in player1.all_items():
                print(f"{item}\n")

        elif desired_request.lower() == 'q':
            is_playing = False

        else:
            print("*****Sorry that is not an option!******\nN for north\nS for south\nE for east\nW for west\nQ to quit\ntake [item name]\ndrop [item name]\n*****Below is your current location*****")
    
    elif len(desired_request_split) == 2:

        if desired_request_split[0].lower() == "take":
            if len(player1.items) == 3:
                print('\n*******SORRRY YOU HAVE TO MANY ITEMS********\n\n*******You must drop an item in order to pick another up*******\n')

            else:
                item_choosen = [item for item in player1.current_room.items if item.name == desired_request_split[1].lower()]
                if len(item_choosen) > 0:
                    print("item exist", item_choosen)
                    player1.add_item(item_choosen[0])
                    player1.current_room.item_picked_up(item_choosen[0])
                else:
                    print("\n*******item doesn't exist in this room******\n")
            
        elif desired_request_split[0].lower() == "drop":
            item_choosen = [item for item in player1.items if item.name == desired_request_split[1].lower()]
            if len(item_choosen) > 0:
                print("item exist in inventory")
                player1.drop_item(item_choosen[0])
                player1.current_room.item_droped(item_choosen[0])
            else: 
                print("\n*******You don't currently have that item in your inventory******\n")

        else:
            print("*****Sorry that is not an option!******\nN for north\nS for south\nE for east\nW for west\nQ to quit\ntake [item name]\ndrop [item name]\n*****Below is your current location*****")

    else:
        print("*****Sorry that is not an option!******\nN for north\nS for south\nE for east\nW for west\nQ to quit\ntake [item name]\ndrop [item name]\n*****Below is your current location*****")