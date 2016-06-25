class Player(object):
    """A simple model of a player"""

    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.deck = []
        self.hand = []
        self.defense = 30
        self.armor = 0
        self.mana_limit = 1
        self.mana = 1
        self.active = True
        self.attack = 0
        self.Frozen = False
        self.times_fatigued = 0

    def change_turn(self):
        print self.name.title() + " turn has ended."

    def update_defense(self, damage):
        if self.armor > 0:
            self.defense = self.defense - max(0, damage - self.armor)
            self.armor = min(0, self.armor - damage)
        else:
            self.defense = self.defense - damage
