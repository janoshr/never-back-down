# event configurations


def werewolf_attack_draw_hand(player):
    """
    Modify draw 4 cards function by event
    """
    pass

def werewolf_attack(players):
    """
    Handles fight event
    """
    Table(players, werewolf_attack_draw_hand)

event_werewolf_attack = {
    'name': 'Werewolves!!',
    'id': 'ww01',
    'effect': werewolf_attack,
}

"""
One event list belongs to a single event chain
"""
event_list = [event_werewolf_attack]
