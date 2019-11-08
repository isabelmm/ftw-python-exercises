#exercise 7
class Car:

	def __init__(self,year,make,model):
		self.year = year
		self.make = make
		self.model = model

	def age(self):
		return 2019 - self.year

my_car = Car(2015,"Toyota","Fortuner")
print(my_car.age())