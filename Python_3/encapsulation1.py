class Millas:
	def __init__(self):
		self._distancia = 0

	# DistanciaGetter
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# DistanciaSetter
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# DistanciaDelete
	def eliminar_distancia(self):
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

def run():
	avion = Millas()
	avion.distancia = 200
	print(avion.distancia)

if __name__ == "__main__":
    run()