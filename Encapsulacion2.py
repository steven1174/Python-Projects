class Millas:
	def __init__(self):
		self._distancia = 0

	# DistanciaGetter: Usando decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# DistanciaSetter:Usando decorador
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

def run():
    avion = Millas()
    avion.distancia = 200

if __name__ == "__main__":
    run()