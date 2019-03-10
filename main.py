from Corredor import Corredor
from Corrida import Corrida
from Turn import Turn

file_open = open('text.txt').readlines()

corrida = Corrida(1)

for i in file_open[1:]:
    hours = i[1:12]
    codigo = i[18:21]
    name = i[24:39]
    turn = i[58:59]

    if not corrida.is_corredor_exist(codigo):
        corredor = Corredor(codigo, name)
        corrida.add_corredor(corredor)

    turn = Turn(3, turn, 1)

    corrida.add_turn(codigo, turn)

corrida.print_result()

