class Hero():

    def hero_equipment(self):
        self.equipment = {'head': None,
                     'body': None,
                     'left_hand': None,
                     'right_hand': None,
                     'legs': None,
                     'boots': None}

    def equipment_output(self):
        print('          ', '[   ', self.equipment['head'], '   ]')
        print('[   ', self.equipment['left_hand'], '   ]', '[   ', self.equipment['body'], '   ]', '[   ', self.equipment['right_hand'], '   ]')
        print('          ', '[   ', self.equipment['legs'], '   ]')
        print('          ', '[   ', self.equipment['boots'], '   ]')

    def hero_inventory(self):
        self.inventory = []

    def __init__(self, name, health, mana, damage):
        self.name = name
        self.health = health
        self.mana = mana
        self.gold = 0
        self.damage = damage
        self.hero_equipment()
        self.hero_inventory()

    def take_item(self, item):
        self.inventory.append(item)

    def take_gold(self, gold):
        self.gold += gold

    def equip_item(self, item, slot):
        if self.equipment[slot] != '':
            self.inventory.append(self.equipment[slot])
        self.equipment.setdefault(slot, item)
