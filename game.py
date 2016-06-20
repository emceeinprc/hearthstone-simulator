# TODO: think about how to ensure only the targetted card (and not other
# instances of that card) gets attacked

from player import Player
from card import Card
import random

# Define the cards available
# TODO: Add logic that auto-increments if duplicates of a card are played
wisp = Card('Wisp', 0, 1, 1)
sergeant = Card('Sergeant', 1, 1, 1)
blood_imp = Card('Blood Imp', 1, 1, 1)
belcher = Card('Belcher', 4, 5, 5)
flame_imp = Card('Flame Imp', 1, 3, 2)

deathlord = Card('Deathlord', 3, 2, 8)
raid_leader = Card('Raid Leader', 3, 2, 2)
shade_of_naxxramus = Card('Shade of Naxxramus', 3, 2, 2)
loot_hoarder = Card('Loot Hoarder', 2, 2, 1)
piloted_shredder = Card('Piloted Shredder', 4, 4, 3)
frostwolf_warlord = Card('Frostwolf Warlord', 5, 4, 4)
emperor_thaurissan = Card('Emperor Thaurissan', 6, 5, 5)
dr_boom = Card('Dr Boom', 7, 7, 7)

# Initialize two players
player1 = Player('Anduin', 'priest')
player2 = Player('Jaina', 'mage')

# Create a board
# The opponent (player2) shows up visually on the top half of the board
# Therefore, player2's board is indexed 1 .. 7 and player1's board is 8 .. 14
board = [player2]
[board.append("[ ]") for i in range(14)]
board.append(player1)

def initialize_universe():
    print "Here. We. Go."

    # Assemble the cards into a list
    card_library = []
    card_library.append(wisp)
    card_library.append(sergeant)
    card_library.append(blood_imp)
    card_library.append(belcher)
    card_library.append(flame_imp)
    card_library.append(deathlord)
    card_library.append(raid_leader)
    card_library.append(shade_of_naxxramus)
    card_library.append(loot_hoarder)
    card_library.append(piloted_shredder)
    card_library.append(frostwolf_warlord)
    card_library.append(emperor_thaurissan)
    card_library.append(dr_boom)

    # Fill the players' list with those cards
    for card in card_library:
        player1.deck.append(card)
        player2.deck.append(card)

    # Create a board


    # Set player 1 to be the only active player
    player2.active = False
    player2.mana_limit = 0

    # Have player 1 draw their first card and play
    draw_card(player1)
    new_turn()


def reset():
    """ Reset all playing conditions """

    # Reset player health
    player1.defense = 30
    player2.defense = 30

    # Reset player mana
    player1.mana = 1
    player1.mana_limit = 1
    player2.mana = 1
    player2.mana_limit = 1

    # Clear cards from board, hands, and deck
    del player1.board[0:len(player1.board)]
    del player1.hand[0:len(player1.hand)]
    del player1.deck[0:len(player1.deck)]

    del player2.board[0:len(player2.board)]
    del player2.hand[0:len(player2.hand)]
    del player2.deck[0:len(player2.deck)]

    # Repopulate decks
    initialize_universe()


def status():
    """ Reports the status of the game """

    # Whose turn is it, anyway?
    active_player = fetch_active_player()
    print "%s (%r hp, %s/%r mana) is playing!" % (active_player.name.title(), active_player.defense, active_player.mana, active_player.mana_limit)

    # What is the opponent's status?
    passive_player = fetch_passive_player()
    print "%s (%r hp) is waiting.\n" % (passive_player.name.title(), passive_player.defense)

    #What can the current player see?
    print_board()
    print "\n"
    print_hand(active_player)
    print "\n"
    cards_visible()


def print_deck(player):
    """Cycle through all cards in deck and print each one"""
    print player.name.title() + "'s deck has " + str(len(player.deck)) + " cards: "
    for i in xrange(0, len(player.deck)):
        print "%s %s mana (%r/%s)" % (player.deck[i].name, player.deck[i].mana, player.deck[i].attack, player.deck[i].defense)


def print_hand(player):
    """Cycle through all cards in hand and print each one"""
    print player.name.title() + "'s hand has " + str(len(player.hand)) + " cards: "
    for i in xrange(0, len(player.hand)):
        print "%s %s mana (%r/%s)" % (player.hand[i].name, player.hand[i].mana, player.hand[i].attack, player.hand[i].defense)


def print_board():
    print "%s (%r hp)" % (board[0].name, board[0].defense)
    for i in range(1, len(board)-1):
        if isinstance(board[i], str):
            print "%s: %s" % (i, board[i])
        else:
            print "%s: %s (%r/%s)" % (i, board[i].name, board[i].attack, board[i].defense)

        if i == 7:
            print "\n"
    print "%s (%r hp)" % (board[15].name, board[15].defense)


#def print_board(player):
#    """Cycle through all cards on board and print each one"""
#    print player.name.title() + "'s board has " + str(len(player.board)) + " cards: "
#    for i in xrange(0, len(player.board)):
#        print "%s %s mana (%r/%s)" % (player.board[i].name, player.board[i].mana, player.board[i].attack, player.board[i].defense)


def fetch_active_player():
    if player1.active:
        return player1
    else:
        return player2


def fetch_passive_player():
    if player1.active:
        return player2
    else:
        return player1


def end_turn():
    if player1.active:
        player2.active = True
        player1.active = False
    else:
        player2.active = False
        player1.active = True

    active_player = fetch_active_player()

    # Update the mana availability of the new player
    active_player.mana_limit = min(10, active_player.mana_limit + 1)
    active_player.mana = active_player.mana_limit

    # The newly active player draws a card
    draw_card(active_player)

    # The board of the active player is able to attack
    for i in range(15):
        if isinstance(board[i], Card):
            board[i].frozen = False

    new_turn()


def new_turn():
    #user_action = print_instructions()
    #parse_instructions(user_action)
    pass


def cards_visible():
    active_player = fetch_active_player()
    passive_player = fetch_passive_player()

    num_in_player_hand = len(active_player.deck)
    num_in_opponent_hand = len(passive_player.hand)
    num_in_opponent_deck = len(passive_player.deck)
    print "The player has " + str(num_in_player_hand) + " cards left in their deck. The opponent has " + str(num_in_opponent_hand) + " cards in their hand and " + str(num_in_opponent_deck) + " in their deck"
    return num_in_player_hand, num_in_opponent_hand, num_in_opponent_deck


def draw_card(player):
    """Cause fatigue if no cards are in deck"""
    if len(player.deck) == 0:
        player.defense = player.defense - 1
        print "The player has been fatigued! You now have " + str(player.defense) + " hp."

        # Check if player has been defeated
        if player.defense <= 0:
            defeat(player)
        return

    # First, choose a card from the deck and make a copy of it
    card_location = random.randint(0, len(player.deck) - 1)
    new_card = player.deck[card_location]

    # Remove the original from the deck
    del player.deck[card_location]

    # Then add the copy to the player's hand
    player.hand.append(new_card)

    # Report what happens
    print player.name.title() + " has drawn " + new_card.name


def play_card(card, position):
    active_player = fetch_active_player()

    # Handle exceptions
    if card not in active_player.hand:
        print "You don't have this card in your hand"
        return

    if active_player.mana < card.mana:
        print "Mana insufficient :("
        return

    if position == 0 or position == 15:
        print "You can't do that"
        return

    if active_player == player1 and position < 7:
        print "You need to put the card on YOUR board"
        return

    if active_player == player2 and position > 8:
        print "You need to put the card on YOUR board"
        return

    # Add the card to the board
    board[position] = card
    card.position = position

    # Remove the card from the player's hand
    active_player.hand.remove(card)

    # Update the player's mana
    active_player.mana = active_player.mana - card.mana

    # Report what happens
    print active_player.name.title() + " puts " + card.name.title() + " on the board!"


def remove_card(target, player):

    # When the target is a player
    if type(target) == Player and target.defense <= 0:
        defeat(player)
        return

    # When the target is a card
    if type(target == Card) and target.defense <= 0:
        board[target.position] = "[ ]"
        target.position = 0
        print target.name.title() + " is removed from the board"
        return


def attack(source, position):  # target can be either a Card or a Player
    active_player = fetch_active_player()
    passive_player = fetch_passive_player()

    # TODO Ensure the target is valid
    if source not in board:
        print "You can't do that"
        return

    if isinstance(board[position], str):
        print "That is not a valid target"
        return

    if source.frozen:
        print "This character cannot attack now"
        return
    # Describe what is happening
    print source.name.title() + " is attacking " + board[position].name.title() + ", which has " + str(board[position].defense) + " hp!"

    # Update the defenses
    board[position].update_defense(source.attack)
    source.update_defense(board[position].attack)

    # Describe the outcome
    print board[position].name.title() + " now has " + str(board[position].defense) + " hp"

    # Check if cards to be removed, and remove if so
    remove_card(source, active_player)
    remove_card(board[position], passive_player)


def defeat(player):
    print player.name.title() + " has been defeated!"


def lookup_target(target):
    active_player = fetch_active_player()
    passive_player = fetch_passive_player()

    new_card = target
    for i in xrange(0, len(passive_player.board)):
        if board[i] == target:
            print i


def print_instructions():
    print "What action do you want to take?"
    print "'E' to end turn"
    print "'S' to see the board"
    print "Type a card name to play the card"
    print "Type 'Attack, source, target' to attack the target with the source"
    user_action = raw_input("Or 'quit' to quit: ")
    return user_action


def parse_instructions(user_action):
    if user_action == 'E':
        end_turn()
    elif user_action == 'S':
        status()
    elif user_action == 'quit':
        exit()
    else:
        print "I'm not smart enough to do that yet"


def taunt(card):
    card.taunt = True

# Initialize the game
initialize_universe()
