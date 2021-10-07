S = 0 #Bandera SOLUCION, encargada de ver si
def encontrar_ruta(C):
	global S
	R = [[0 for x in range(len(C[0]))] for y in range(len(C))]
	x = 0 #Ancho
	y = 0 #Largo
	A = encontrar_rutaAUX(C,x,y,R)
	if(S == 1):
		S -= 1
	return A
def encontrar_rutaAUX(C,x,y,R):
	global S
	if 0<=y and y<(len(C[0])) and 0<=x and x<(len(C)) and S == 0: #Cuando los indices no se salen de los limites de la matriz
		if C[x][y] == 0: #Cuando se ha encontrado una interseccion segura
			if y == (len(C[0])-1) and x == (len(C)-1) and C[x][y] == 0:# Cuando se llega al punto de llegada y no hay interseccion peligrosa; se encuentra una ruta
				print ("Encontrado")
				S += 1
				R[x][y] = 1
			else:
				C[x][y] = 7
				R[x][y] = 1
				encontrar_rutaAUX(C,x+1,y,R)		
				encontrar_rutaAUX(C,x,y+1,R)
				encontrar_rutaAUX(C,x-1,y,R)
				encontrar_rutaAUX(C,x,y-1,R)
				if(S==1):
					return R
				else:
					R[x][y] = 0
					if R == [[0 for x in range(len(C[0]))] for y in range(len(C))]:
						R = []
						return R