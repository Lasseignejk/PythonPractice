class Vehicle: 
	def __init__(self, make, model):
		self.make = make
		self.model = model

	def moves(self):
		print("Moves along...")
	
	def get_make_model(self):
		print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('VW', 'Taos')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle): 
	def __init__(self, make, model, faa_id):
		super().__init__(make, model)
		self.faa_id = faa_id
	def moves(self):
		print('Flies along...')
	def get_call_num(self):
		print(f"Call sign: {self.faa_id}")
	
class Truck(Vehicle):
	def moves(self): 
		print('Rumbles along...')
	
class GolfCart(Vehicle): 
	pass

cessna = Airplane('Cessna', 'Skyhawk', 'SLH700')
mack = Truck('Mack', 'Pinnacle')
golf_wagon = GolfCart('Yamaha', 'GC100')

cessna.moves()
mack.moves()
golf_wagon.moves()