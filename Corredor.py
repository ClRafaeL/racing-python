class Corredor():
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name
        self.turns = []
        self.position = 9

    def add_turn(self, turn):
        self.turns.append(turn)
        if len(self.turns) == 4:
            return True

        return False

    def print(self):
        print(self.cod, self.name)
    
    def calc_time_med(self):
        total = 0
        for turn in self.turns:
            total += turn.time
        return total / self.turns.__len__()