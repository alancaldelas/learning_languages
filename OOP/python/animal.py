"""
Alan Caldelas
"""

class Animal:
	"""
	Simple Animal Class
	"""
	animal_name = "Animal"
	legs = 4
	kind = "Unknown"
	
	def __init__(self, name):
		self.name = name
	
	def set_type(self, kind):
		self.kind = kind
		return self.kind

	def name(self):
		self.animal_name = animal_name
		return animal_name

	def name(self, name):
		self.animal_name = name
		return self.animal_name


def main ():
	print("Object oriented animal class")
	x = Animal()
	print(x.animal_name)
	print(x.name("Ted"))


main()

