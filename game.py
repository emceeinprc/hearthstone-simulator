from player import Player
from card import Card
import random

# Define the cards available
wisp = Card('Wisp', 0, 1, 1)
sergeant = Card('Sergeant', 1, 1, 1)
blood_imp = Card('Blood Imp', 1, 1, 1)
belcher = Card('Belcher', 4, 5, 5)
flame_imp = Card('Flame Imp', 1, 3, 2)

# Initialize two players
anduin = Player('Anduin', 'priest')
jaina = Player('Jaina', 'mage')

def initialize_universe():
    # Assemble the cards into a list
    card_library = []
    card_library.append(wisp)
    card_library.append(sergeant)
    card_library.append(blood_imp)
    card_library.append(belcher)

    # Fill the players' list with those cards
    for i in xrange(0, len(card_library)):
        anduin.deck.append(card_library[i])
        jaina.deck.append(card_library[i])

def print_deck(player):
    # Cycle through all cards in deck and print each one
    print player.name.title() + "'s deck has " + str(len(player.deck)) + " cards: "
    for i in xrange(0, len(player.hand)):
        print str(player.hand[i].name)

def print_hand(player):
    # Cycle through all cards in hand and print each one
    print player.name.title() + "'s hand has " + str(len(player.hand)) + " cards: "
    for i in xrange(0, len(player.hand)):
        print str(player.hand[i].name)

def print_board(player):
    # Cycle through all cards on board and print each one
    print player.name.title() + "'s board has " + str(len(player.hand)) + " cards: "
    for i in xrange(0, len(player.hand)):
        print str(player.hand[i].name)

def draw_card(player):
    # Cause fatigue if no cards are in deck
    if len(player.deck) == 0:
        player.defense = player.defense -1
        print "The player has been fatigued! You now have " + str(player.defense) + " hp."
        return

    # First, choose a card from the deck and make a copy of it
    card_location = random.randint(0, len(player.deck) - 1)
    new_card = player.deck[card_location]

    # Remove the original from the deck
    del player.deck[card_location]

    # Then add the copy to the player's hand
    player.hand.append(new_card)

def play_card(player, card):
    # Add the card to the board
    player.board.append(card)

    # Remove the card from the player's hand
    player.hand.remove(card)

def remove_card(target):
    if target.defense <= 0:
        print target.name.title() + " is removed from the board"

def attack(player, source, target):
    # target can be either a Card or a Player

    # describe what is happening
    print source.name.title() + " is attacking " + target.name.title() + ", which has " + str(target.defense) + " hp!"

    # update the defense of the attacker
    target.update_defense(source.attack)

    print target.name.title() + " now has " + str(target.defense) + " hp"
    remove_card(target)

# A series of actions to simulate the game
initialize_universe()
draw_card(anduin)
draw_card(anduin)
draw_card(anduin)
draw_card(anduin)
play_card(anduin, wisp)
play_card(anduin, belcher)
#print_hand(anduin)
attack(anduin, wisp, jaina)
