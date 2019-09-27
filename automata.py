import time

automata2 = [[1, 0, None, None],
             [None, None, 0, 1],
             [None, None, [0, 1], None],
             [None, None, None, 0]]

automata = [[None, 0, None, None],
            [None, None, 0, 1],
            [None, None, None, 1],
            [None, None, None, None]]

automata3 = [[None, 0],
             [0, None]]

estados_aceptacion = [0]


def recorrer(automata, estados_recorridos=None, estado_actual=0):
    estados_recorridos_iteracion = estados_recorridos.copy() if estados_recorridos else []
    print(f"Recorriendo desde {estado_actual}: estados recorridos {estados_recorridos_iteracion}")
    for estado_siguiente in range(len(automata)):
        if automata[estado_actual][estado_siguiente] != None:
            # Caso 1: q_i -> q_i
            if estado_actual == estado_siguiente:
                raise Exception("pailamifai")

            # Caso 2: ya he estado en ese estado

            print(f"estado en revision [origen {estado_actual}][destino {estado_siguiente}]")
            # if estado_anterior+1 in estados_recorridos:
            if estado_siguiente in estados_recorridos_iteracion:
                raise Exception("pailamifai2")

            print("agregando a recorridos ", estado_siguiente)
            estados_recorridos_iteracion.append(estado_siguiente)
            print(f"recorridos {estados_recorridos_iteracion}")
            recorrer(automata, estados_recorridos_iteracion, estado_siguiente)
    print(f"Finalizado recorrido desde {estado_actual}")


recorrer(automata)
print("ta bien")
