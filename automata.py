import time


def recorrer(automata):
    def buscar_ciclos(automata, estados_recorridos=None, estado_actual=0):
        estados_recorridos_iteracion = (
            estados_recorridos.copy() if estados_recorridos else []
        )
        for estado_siguiente in range(len(automata["matriz_transicion"])):
            if automata["matriz_transicion"][estado_actual][estado_siguiente] != None:
                if estado_siguiente in estados_recorridos_iteracion:
                    return False

                estados_recorridos_iteracion.append(estado_siguiente)
                if not buscar_ciclos(
                    automata, estados_recorridos_iteracion, estado_siguiente
                ):
                    return False

        if (
            automata["matriz_transicion"][estado_actual]
            == [None] * len(automata["matriz_transicion"])
            and estado_actual not in automata["estados_aceptacion"]
        ):
            return False

        return True

    reconoce_lenguaje_finito = buscar_ciclos(automata)
    if reconoce_lenguaje_finito:
        print("El automata reconoce un lenguaje finito")
    else:
        print("El automata reconoce un lenguaje infinito")


automata_lenguaje_finito = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None],
        [None, None, ["a", "b"]],
        [None, None, None],
    ],
    "estados_aceptacion": [2],
}


automata_lenguaje_finito2 = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None],
        [None, None, None],
        [None, None, None],
    ],
    "estados_aceptacion": [1],
}

automata_lenguaje_infinito = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None, None],
        [None, None, "a", "b"],
        [None, None, None, "b"],
        [None, None, None, "b"],
    ],
    "estados_aceptacion": [2, 3],
}

automata_lenguaje_infinito2 = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None, None],
        [None, None, "a", "b"],
        [None, None, None, ["a", "b"]],
        [None, None, "a", None],
    ],
    "estados_aceptacion": [1, 2, 3],
}

recorrer(automata_lenguaje_finito)
recorrer(automata_lenguaje_finito2)
recorrer(automata_lenguaje_infinito)
recorrer(automata_lenguaje_infinito2)
