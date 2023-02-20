class CasillaDeVotacion:

	def __init__(self,identificador,pais):
		self.__identificador = identificador
		self.__pais = pais
		self.__region = None

	# RegionGetter
	@property
	def region(self):
		return self.__region

	# RegionSetter
	@region.setter
	def region(self, region):
		if region in self.__pais:
			self.__region = region
		else:
			raise ValueError(f'La region {region} no es valida en {self.__pais}')

def run():
	casilla = CasillaDeVotacion(123,['CDMX','Morelos'])
	print(casilla.region)
	casilla.region = 'CDMX'
	print(casilla.region)

if __name__ == "__main__":
    run()