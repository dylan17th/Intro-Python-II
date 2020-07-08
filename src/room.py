# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
    
    def show_items_in_room(self):
        for item in self.items:
            print(f"name: {item.name}, description: {item.description}")

    def item_picked_up(self, item):
        pass