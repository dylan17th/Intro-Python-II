# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def current_room_nice_print(self):
        print(f"Name of current Room: {self.current_room.name}\nDescription: {self.current_room.description}")

    def add_item(self, item):
        if len(self.items) >= 3:
            print('*******SORRRY YOU HAVE TO MANY ITEMS********')
        else:
            self.items.append(item)

    def drop_item(self, item):
        if len(self.items) == 0:
            print('*******SORRRY YOU HAVE TO MANY ITEMS SO YOU CAN NOT DROP ANY********')
        else: 
            self.items.remove(item)   

    def all_items(self):
        if len(self.items) > 0:
            for item in self.items:
                print(f"Name:{item.name}\nDescription:{item.desciption} ")
        else:
            print("*****You Currently have no items******")
