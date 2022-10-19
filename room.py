class Room:

    number_of_rooms = 0

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self._room_item = None
        Room.number_of_rooms += 1

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)

    @property
    def room_item(self):
        return self._room_item

    @room_item.setter
    def room_item(self, room_item):
        self._room_item = room_item

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        if self.room_item is not None:
            print(f"Item to pick: {self.room_item.get_name()}")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
