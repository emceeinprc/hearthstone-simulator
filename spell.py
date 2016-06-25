class Spell(object):
    """A Hearthstone spell"""

    # List of properties
    # offense: how much damage is done (int)
    # requires target: does the spell require a target (boolean)
    # defense_health: how much health is added (int)
    # defense_armor: how much armor is added (int)
    # spread: (string)
    #   'target': affects the targeted character only
    #   'target plus adjacent': affects the targeted character plus adjacent ones
    #   'enemy': targets enemies
    #   'enemy minions': targets enemy minions
    #   'friendly minions': targets your minions
    #   'all characters': affects all characters on board
    # spread_random: whether or not the target(s) is(are) random (boolean)
    # num_targets: number of characters targetted by the spell (int)

    def __init__(self, name, mana, properties):
        """Initialize spell attributes"""
        self.name = name
        self.mana = mana
        self.properties = properties
