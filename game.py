from player import Player
from card import Card
import random

# Define the cards available
#TODO: Add logic that auto-increments if duplicates of a card are played
wisp = Card('Wisp', 0, 1, 1)
sergeant = Card('Sergeant', 1, 1, 1)
blood_imp = Card('Blood Imp', 1, 1, 1)
belcher = Card('Belcher', 4, 5, 5)
flame_imp = Card('Flame Imp', 1, 3, 2)

# Initialize two players
player1 = Player('Anduin', 'priest')
player2 = Player('Jaina', 'mage')
active_player = player1
passive_player = player2

def initialize_universe():
    # Assemble the cards into a list
    card_library = []
    card_library.append(wisp)
    card_library.append(sergeant)
    card_library.append(blood_imp)
    card_library.append(belcher)

    # Fill the players' list with those cards
    for i in xrange(0, len(card_library)):
        player1.deck.append(card_library[i])
        player2.deck.append(card_library[i])

def print_deck(player):
    # Cycle through all cards in deck and print each one
    print player.name.title() + "'s deck has " + str(len(player.deck)) + " cards: "
    for i in xrange(0, len(player.deck)):
        print str(player.deck[i].name)

def print_hand(player):
    # Cycle through all cards in hand and print each one
    print player.name.title() + "'s hand has " + str(len(player.hand)) + " cards: "
    for i in xrange(0, len(player.hand)):
        print str(player.hand[i].name)

def print_board(player):
    # Cycle through all cards on board and print each one
    print player.name.title() + "'s board has " + str(len(player.board)) + " cards: "
    for i in xrange(0, len(player.board)):
        print str(player.board[i].name)

def end_turn(player):
    # Pass the turn to the opponent
    if active_player == player1:
        active_player = player2
        passive_player = player1
    else:
        active_player = player1
        passive_player = player2

    # The newly active player draws a card
    draw_card(active_player)

def draw_card(player):
    # Cause fatigue if no cards are in deck
    if len(player.deck) == 0:
        player.defense = player.defense - 1
        print "The player has been fatigued! You now have " + str(player.defense) + " hp."
        return

    # First, choose a card from the deck and make a copy of it
    card_location = random.randint(0, len(player.deck) - 1)
    new_card = player.deck[card_location]

    # Remove the original from the deck
    del player.deck[card_location]

    # Then add the copy to the player's hand
    player.hand.append(new_card)

def play_card(card):
    # Add the card to the board
    active_player.board.append(card)

    # Remove the card from the player's hand
    active_player.hand.remove(card)

def remove_card(target):
    if target.defense <= 0:
        #TODO: Need to remove this card from the board
        passive_player.board.remove(target)

        print target.name.title() + " is removed from the board"

def attack(source, target): # target can be either a Card or a Player
    # Describe what is happening
    print source.name.title() + " is attacking " + target.name.title() + ", which has " + str(target.defense) + " hp!"

    # Update the defense of the attacker
    target.update_defense(source.attack)

    # Describe the outcome
    print target.name.title() + " now has " + str(target.defense) + " hp"

    # Check if cards to be removed, and remove if so
    remove_card(target)

# A series of actions to simulate the game
initialize_universe()
draw_card(player1)
draw_card(player1)
draw_card(player1)
draw_card(player1)
print_deck(player1)
print_hand(player1)
print_board(player1)
play_card(wisp)
play_card(belcher)
print_hand(player1)
print_board(player1)
attack(wisp, player2)
