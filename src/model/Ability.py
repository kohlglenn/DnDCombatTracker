class Ability:
    attack_bonus: int # can be NULL
    desc: str
    name: str
    damage_bonus: int  # can be NULL
    damage_dice: str  # can be NULL

    def __init__(self, attack_bonus, desc, name, damage_bonus, damage_dice):
        self.attack_bonus = attack_bonus
        self.desc = desc
        self.name = name
        self.damage_bonus = damage_bonus
        self.damage_dice = damage_dice


def create_special_ability(name, desc):
    return Ability(None, desc, name, None, None)
