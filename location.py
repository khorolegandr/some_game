import random

equip_vars = ['broken_helmet', 'broken_cuirass', 'broken_sword', 'broken_shield', 'broken_greaves', 'broken_boots']

class Events():

    pass

class Floor():

    def loc_generation(self):
        room_examples = ['[x]', 0, 0, 0, 1, 1, 1, 2, 2, 2]
        location = [['[x]' for j in range(self.size[1] + 2)] for i in range(self.size[0] + 2)]
        for i in range(1, len(location) - 1):
            for j in range(1, len(location[0]) - 1):
                location[i][j] = room_examples[random.randint(0, 9)]
        lvl_entrance = random.randint(1, self.size[0] * self.size[1])
        lvl_exit = random.randint(1, self.size[0] * self.size[1])
        while lvl_exit == lvl_entrance:
            lvl_exit = random.randint(0, (len(location) * len(location[0]) - 1))
        counter = 0
        for i in range(1, self.size[0] + 1):
            for j in range(1, self.size[1] + 1):
                counter += 1
                if counter == lvl_entrance:
                    location[i][j] = 0
                    location[i][j] = str(location[i][j]) + '_^_'
                elif counter == lvl_exit:
                    location[i][j] = 0
                    location[i][j] = str(location[i][j]) + '_v_'
        return location

    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.shape = self.loc_generation()
        self.loc_mirror = self.shape.copy()

    def output(self):
        output_str = ''
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                output_str += (str(self.loc_mirror[i][j]).ljust(8))
                output_str += ' '

        output_str.encode('utf-8')
        return output_str
