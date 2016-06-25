class Card(object):
    """A Hearthstone card"""

    sleep = "[Zzz]"
    taunt = "[Taunt]"
    divine_shield = "[Divine Shield]"
    stealth = "[Stealth]"

    def __init__(self, name, mana, attack, defense, has_taunt=False, has_divine_shield=False, has_stealth=False):
        """Initialize card attributes"""
        self.name = name
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.starting_defense = defense
        self.frozen = True
        self.has_taunt = has_taunt
        self.has_divine_shield = has_divine_shield
        self.has_stealth = has_stealth
        self.position = 0
        self.tags = []

    def play(self):
        print self.name.title() + " is on the board."

    def battlecry(self):
        print self.name.title() + " does its battlecry"

    def update_defense(self, damage):
        if self.has_divine_shield and damage > 0:
            self.has_divine_shield = False
        else:
            self.defense = self.defense - damage

    def reset(self):
        self.defense = self.starting_defense

    def generate_tags(self):
        self.tags = []
        if self.frozen:
            self.tags.append(self.sleep)
        if self.has_taunt:
            self.tags.append(self.taunt)
        if self.has_divine_shield:
            self.tags.append(self.divine_shield)
        if self.has_stealth:
            self.tags.append(self.has_stealth)
        return ' '.join(self.tags)
