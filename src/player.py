# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def player_move(self, direction):
        str = f"{direction}_to"
        new_room = getattr(self.current_room, str)
        if new_room:
            self.current_room = new_room
        else:
            print("can't go that way, try a different direction")
    def __str__(self):
        return f'{self.name} is currently in {self.current_room}'
