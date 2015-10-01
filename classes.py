class MyClass:
	"""A simple example class"""
	i = 7
	def __init__(self):
		self.i = 5

	def f(self, a_int):
		return self.i + a_int

myClass = MyClass()
print(myClass.f(3))

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
complex = Complex(1, 2)
print(complex.r, complex.i)
