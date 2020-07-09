class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
    
    def show_items_in_room(self):
        return [f"name: {item.name}, description: {item.description}" for item in self.items]

    def item_picked_up(self, item):
        self.items.remove(item)

    def item_droped(self, item):
        self.items.append(item)
    