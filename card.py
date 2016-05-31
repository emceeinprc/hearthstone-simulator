class Card(object):
    """A Hearthstone card"""

    def __init__(self, name, mana, attack, defense):
        """Initialize card atttributes"""
        self.name = name
        self.mana = mana
        self.attack = attack
        self.defense = defense

#    def attack(self):
#        return 2

    def play(self):
        print self.name.title() + " is on the board."

    def battlecry(self):
        print self.name.title() + " does its battlecry"

    def update_defense(self, damage):
        self.defense = self.defense - damage
