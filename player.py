class Player(object):
    """A simple model of a player"""

    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.deck = []
        self.hand = []
        self.board = []
        self.defense = 30

    def change_turn(self):
        print self.name.title() + " turn has ended."

    def update_defense(self, damage):
        self.defense = self.defense - damage
