class Player(object):
    """A simple model of a player"""

    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.deck = []
        self.hand = []
        self.board = []
        self.defense = 30
        self.mana_limit = 1
        self.mana = 1
        self.active = True
        self.attack = 0
        self.Frozen = False

    def change_turn(self):
        print self.name.title() + " turn has ended."

    def update_defense(self, damage):
        self.defense = self.defense - damage
