import random
import hero
import location

def create_hero():
    name = 'Hero'
    health = 100
    mana = 20
    damage = 10

    new_hero = hero.Hero(name, health, mana, damage)
    return new_hero

def create_floor():
    number = 1
    size = (width, leight) = (6, 6)

    new_floor = location.Floor(number, size)
    return new_floor

def entrance_to_floor(floor, hero):
    for i in range(len(floor.loc_mirror)):
        for j in range(len(floor.loc_mirror[0])):
            if floor.loc_mirror[i][j] == '0_^_':
                if '0' in floor.loc_mirror[i][j]:
                    floor.loc_mirror[i][j] = '{ hero }'
                elif '1' in floor.loc_mirror[i][j]:
                    floor.loc_mirror[i][j] = '{ hero }'
                    event(1)
                    floor.shape[i][j] = 0
                elif '2' in floor.loc_mirror[i][j]:
                    floor.loc_mirror[i][j] = '{ hero }'
                    event(2)
                    floor.shape[i][j] = 0
    return floor.loc_mirror


def room_entrance(floor, i, j, i0, j0):
    floor.loc_mirror[i0][j0] = floor.shape[i0][j0]
    if floor.shape[i][j] == 0:
        floor.loc_mirror[i][j] = '{ hero }'
        floor.shape[i][j] = 0
    elif floor.shape[i][j] == 1:
        floor.loc_mirror[i][j] = '{ hero }'
        event(1)
        floor.shape[i][j] = 0
    elif floor.shape[i][j] == 2:
        floor.loc_mirror[i][j] = '{ hero }'
        event(2)
        floor.shape[i][j] = 0

    if floor.shape[i][j] == '0_v_':
        answer = input('Do you wanna go down? [y/n]: ')

def loot():
    gold = random.randint(0, 10)
    equipment = random.sample(location.equip_vars, random.randint(0, 3))
    return gold, equipment

def event(num):
    if num == 1:
        hero.health -= 10
    elif num == 2:
        gold, equipment = loot()
        hero.take_gold(gold)
        for item in equipment:
            hero.take_item(item)