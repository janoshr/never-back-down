import random

class Card:
    def __init__(self, name, id, card_type):
        self.name = name
        self.id = id
        self.card_type = card_type

class Weapon(Card):

    def __init__(self, name, id, card_type):
        super().__init__(name, id, card_type)

        if 'sword' in self.card_type:
            self.damage = 3
            self.miss = 0.0
            self.crit = 0.0
            self.crit_damage = 3
        elif 'bow' in self.card_type:
            self.damage = 2
            self.miss = 0.2
            self.crit = 0.1
            self.crit_damage = 4
        # TODO: other card types


    def action(self, acting_player, target_player, opponent_card):
        """
        Chopps at target player, if hit then damage dealt++
        Ranged weapon doe not get parried
        If parry then target_player damage dealt ++
        """
        if random.random() < self.miss:
            return
        if 'shield' in opponent_card.card_type:
            parry_damage = opponent_card.block()
            if parry_damage and 'melee' in self.card_type:
                acting_player.lose_health(parry_damage)
                target_player.damage_dealt_in_fight+=parry_damage
                return
            elif parry_damage == 0:
                return

        damage = self.damage
        if  random.random() < self.crit:
            damage = self.crit_damage
        target_player.lose_health(damage)
        acting_player.damage_dealt_in_fight+=damage



# class Spell:
#     name
#     id
#     description
#     card_type

class Shield(Card):

    def __init__(self, name, id, card_type):
        super().__init__(name, id, card_type)
        self.block_chance = 0.75
        self.parry_damage = 1

    def block(self ):
        if random.random() < self.block_chance:
            return parry_damage
        else:
            return None

base_cards = [
Weapon('Rusty sword', random.randint(0,65536), ['sword', 'melee']),
Weapon('Family breadknife', random.randint(0,65536), ['sword', 'melee']),
Shield('Wooden Plank', random.randint(0,65536), ['shield']),
Weapon('Grandpa\'s good old shortbow', random.randint(0,65536), ['bow', 'ranged'])
]
cards = [sword_card]
