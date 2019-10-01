import time


def recorrer(automata):
    estados_aceptacion_recorridos_sin_ciclos = set()
    estados_aceptacion_recorridos_con_ciclos = set()
    def buscar_ciclos(automata, estados_recorridos=None, estado_actual=0):
        estados_recorridos_iteracion = (
            estados_recorridos.copy() if estados_recorridos else []
        )
        for estado_siguiente in range(len(automata["matriz_transicion"])):
            if automata["matriz_transicion"][estado_actual][estado_siguiente] != None:
                if estado_siguiente in estados_recorridos_iteracion:
                    if estado_siguiente in automata["estados_aceptacion"]:
                        estados_aceptacion_recorridos_sin_ciclos.remove(estado_siguiente)
                        estados_aceptacion_recorridos_con_ciclos.add(estado_siguiente)
                    return True

                estados_recorridos_iteracion.append(estado_siguiente)

                if estado_siguiente in automata["estados_aceptacion"]:
                    estados_aceptacion_recorridos_sin_ciclos.add(estado_siguiente)

                encontro_ciclos = buscar_ciclos(
                    automata, estados_recorridos_iteracion, estado_siguiente
                )
                if encontro_ciclos:
                    return True

        if estado_actual in automata["estados_aceptacion"]:
            estados_aceptacion_recorridos_sin_ciclos.add(estado_actual)

        return False

    encontro_ciclos = buscar_ciclos(automata)

    reconoce_lenguaje_finito = False

    if encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) == 0 and len(estados_aceptacion_recorridos_con_ciclos) == 0:
        reconoce_lenguaje_finito = False
    elif encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) > 0 and len(estados_aceptacion_recorridos_con_ciclos) == 0:
        reconoce_lenguaje_finito = True
    elif not encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) == 0 and len(estados_aceptacion_recorridos_con_ciclos) == 0:
        reconoce_lenguaje_finito = False
    elif not encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) > 0 and len(estados_aceptacion_recorridos_con_ciclos) == 0:
        reconoce_lenguaje_finito = True
    elif encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) == 0 and len(estados_aceptacion_recorridos_con_ciclos) > 0:
        reconoce_lenguaje_finito = False
    elif encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) > 0 and len(estados_aceptacion_recorridos_con_ciclos) > 0:
        reconoce_lenguaje_finito = False
    elif not encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) == 0 and len(estados_aceptacion_recorridos_con_ciclos) > 0:
        reconoce_lenguaje_finito = False
    elif not encontro_ciclos and len(estados_aceptacion_recorridos_sin_ciclos) > 0 and len(estados_aceptacion_recorridos_con_ciclos) > 0:
        reconoce_lenguaje_finito = False

    if reconoce_lenguaje_finito is True:
        print("El automata reconoce un lenguaje finito")
    elif reconoce_lenguaje_finito is False:
        print("El automata no reconoce un lenguaje finito")

automata_lenguaje_finito = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None, "b"],
        [None, None, "a", "b"],
        [None, None, None, ["a", "b"]],
        [None, None, None, ["a", "b"]],
    ],
    "estados_aceptacion": [2],
}

automata_lenguaje_infinito = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None, "b"],
        [None, None, "a", "b"],
        [None, None, None, ["a", "b"]],
        [None, None, None, ["a", "b"]],
    ],
    "estados_aceptacion": [3],
}

automata_lenguaje_infinito2 = {
    "alfabeto": ["a", "b"],
    "matriz_transicion": [
        [None, "a", None, "b"],
        [None, None, "a", "b"],
        [None, None, None, ["a", "b"]],
        [None, None, None, ["a", "b"]],
    ],
    "estados_aceptacion": [2, 3],
}

recorrer(automata_lenguaje_finito)
recorrer(automata_lenguaje_infinito)
recorrer(automata_lenguaje_infinito2)
