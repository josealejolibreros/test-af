import time

automata2 = [[1,0,None,None],
[None,None,0,1],
[None,None,[0,1],None],
[None,None,None,0]]

automata = [[None,0,None,None],
[None,None,0,1],
[None,None,None,1],
[None,None,None,None]]

estados_aceptacion=[2,3]

def recorrer(automata,estados_recorridos=[],estado_anterior=0):
	for idx_filas in range(estado_anterior,len(automata)):
		for idx_columnas in range(len(automata)):

			if automata[idx_filas][idx_columnas]!=None:
				#Caso 1: q_i -> q_i
				if idx_filas==idx_columnas: 
					raise Exception("pailamifai")

				#Caso 2: ya he estado en ese estado
				
				
				#if estado_anterior+1 in estados_recorridos:
				if idx_columnas in estados_recorridos:
					raise Exception("pailamifai2")

				print("voy a meter el ",idx_columnas)	
				estado_anterior = idx_columnas
				time.sleep(3)
				estados_recorridos.append(estado_anterior)

				recorrer(automata,estados_recorridos,estado_anterior)
	print("ta bien")			


			



recorrer(automata)
