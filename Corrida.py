class Corrida():
    def __init__(self, time_inic):
        self.time_inic = time_inic
        self.corredores = []
        self.winner = None
        self.finished = False
        self.last_position = 0
    
    def add_corredor(self, corredor):
        self.corredores.append(corredor)
    
    def is_corredor_exist(self, cod):
        corredor = self.find_corredor(cod)

        if corredor != None:
            return True
    
        return False

    def add_turn(self, cod, turn):
        corredor = self.find_corredor(cod)

        finish = corredor.add_turn(turn)
        if finish:
            if self.winner == None:
                self.set_winner(corredor)

            self.last_position += 1 
            corredor.position = self.last_position

    def set_winner(self, corredor):
        self.winner = corredor
        self.finished = True

    def find_corredor(self, cod):
        for corredor in self.corredores:
            if corredor.cod == cod:
                return corredor
            
        return None

    def is_finished(self):
        return self.finished

    def print_result(self):
        self.order_corredor()

        print('Posiçao', 'Codigo', 'Nome', 'Voltas')
        for corredor in self.corredores:
            print(corredor.position, corredor.cod, corredor.name,  len(corredor.turns))

    def order_corredor(self):
        for inicial in range(0, len(self.corredores) - 1):
            exchanging = False

            for atual in range(0, len(self.corredores) - 1):
                if self.corredores[atual].position > self.corredores[atual + 1].position:
                    self.corredores[atual], self.corredores[atual + 1] = self.corredores[atual + 1], self.corredores[atual]
                    exchanging = True

            if not exchanging:
                break