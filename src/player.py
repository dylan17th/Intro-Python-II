class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def current_room_nice_print(self):
        return f"Name of current Room: {self.current_room.name}\nDescription: {self.current_room.description}"

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        if len(self.items) == 0:
            return '*******SORRRY YOU HAVE TO MANY ITEMS SO YOU CAN NOT DROP ANY********'
        else: 
            self.items.remove(item)

    def all_items(self):
        if len(self.items) > 0:
                return [f"name: {item.name}, description: {item.description}" for item in self.items]
        else:
            return ["\n*****You Currently have no items******\n"]
