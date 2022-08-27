from cards import base_cards

class Lobby:
    players=[]
    admin

    def __init__(self):
        pass

    def join(self, name):
        """
        Add player to the Lobby
        """
        pass

    def create_game(self):
        """
        create Game
        """
        pass


class Game:
    players=[]
    event_chains=[]
    current_event
    event_counter

    def __init__(self):
        pass

    def next_event(self):
        """
        Choose an event chain and progress to next event
        First x events are from main event chain
        """
        pass

class Player:
    name
    deck=[]
    health
    vitality
    damage_dealt_in_fight
    id

    def __init__(self, name):
        self.name=name
        self.deck=base_cards

    def add_card_to_deck(self):
        pass

    def remove_card_from_deck(self):
        pass

    def lose_health(self):
        pass

    def gain_health(self):
        pass

    def has_card_type(self, card_type, amount):
        pass

    def has_card_id(self, card_id, amount):
        pass

class EventChain:
    index
    event_ids=[]
    name
    def __init__(self, event_ids):
        pass

    def do_next_event(self):
        """
        Move index to next event index
        """
        pass

class Table:
    players_in_fight=[]
    """
    {unplayed_cards,played_cards,activated_card, target_id}
    """
    hands = {}


    def __init__(self, players, draw_4_cards):
        """
        Create hands for each players
        Reset vitality
        """
        pass

    def choose_card(self, player, card, target_id):
        """
        Player chooses a card to act against another,
        or chickens out!!
        Then that player is dropped from hands and players in fight.
        """
        pass

    def resolve_round(self):
        """
        For each player play their card, which deals damage...
        If no players or only 1 player left in fight, then resolve table
        """
        pass

    def resolve_table(self):
        """
        Reset players vitality and return winner.
        In case of tie, no winners
        """
        pass
