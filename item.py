class Item:
    number_of_items = 0

    def __init__(self):
        self.name = None
        self.description = None
        Item.number_of_items += 1

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_details(self):
        print(f'Name: {self.name}\nDescription: {self.description}')
