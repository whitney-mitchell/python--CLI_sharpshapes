import math

class Shape:
	pass

class Circle(Shape):

	def __init__(self, radius):
		self.radius = radius

	def calc_circle_area(self):
		self.area = round(math.pi * (self.radius**2), 2)
		return self.area

	def calc_circle_circ(self):
		self.circ = round((2 * math.pi * self.radius), 2)
		return self.circ

class Cylinder(Circle):

	def __init__(self, radius, height):
		self.radius = radius
		self.height = height

	def calc_cylinder_area(self):
		self.area = round((2 * math.pi * self.radius * self.height  +  2 * math.pi * (self.radius**2)), 2)
		return self.area

	def calc_cylinder_volume(self):
		self.volume = round((math.pi * (self.radius**2) * self.height), 2)
		return self.volume

	def calc_cylinder_circ(self):
		self.circ = self.calc_circle_circ()
		return self.circ

class Square(Shape):

	def __init__(self, height):
		self.height = height

	def calc_square_area(self):
		self.area = round(self.height**2)
		return self.area

class Rhombus(Shape):

	def __init__(self, base, height):
		self.base = base
		self.height = height

	def calc_rhombus_area(self):
		self.area = round((self.base * self.height), 2)
		return self.area

class Cube(Shape):

	def __init__(self, height):
		self.height = height

	def calc_cube_area(self):
		self.area = round(6 * (self.height**2), 2)
		return self.area

	def calc_cube_volume(self):
		self.volume = round(self.height**3, 2)
		return self.volume

def menu():

	print("Select a shape by its number:")
	print("1. Circle \n2. Square \n3. Rhombus \n4. Cube \n5. Cylinder \n6. Quit")

	user_shape = input("> ")

	try:
		if int(user_shape) > 0 and int(user_shape) < 7 :
			# if else statements ---
			if user_shape == "1":
				# next 4 lines in own function? same with each user__shape choice?
				# then, could seperate files by shape, but have the print stuff (like below)
				# inherit from a menu class . . . maybe?
				print("What would you like the radius of your circle to be?")
				radius = int(input("> "))

				results = Circle(radius)
				print("--The area of your circle is " + str(results.calc_circle_area()) + ".")
				print("--The circumference is " + str(results.calc_circle_circ()) + ".\n")

			elif user_shape == "2":
				print("What would you like the length of your square to be?")
				length = int(input("> "))

				results = Square(length)
				print("--The area of your square is " + str(results.calc_square_area()) + ".")
				print("--It has 4 sides.\n")

			elif user_shape == "3":
				print("What would you like the height of your rhombus to be?")
				height = int(input("> "))

				print("What about the length of the base?")
				base = int(input("> "))

				results = Rhombus(base, height)
				print("--The area of your rhombus is " + str(results.calc_rhombus_area()) + ".")
				print("--It has 4 sides.\n")

			elif user_shape =="4":
				print("What would you like the height of your cube to be?")
				height = int(input("> "))

				results = Cube(height)
				print("--The area of your cube is " + str(results.calc_cube_area()) + ".")
				print("--The volume is " + str(results.calc_cube_volume()) + ".")
				print("--And it's a cube, so it has 6 sides.\n")

			elif user_shape =="5":
				print("How tall is this cylinder?")
				height = int(input("> "))

				print("Okay, what about the length of the radius?")
				radius = int(input("> "))

				results = Cylinder(radius, height)
				print("--Your cylinder's area is " + str(results.calc_cylinder_area()) + ".")
				print("--The volume is " + str(results.calc_cylinder_volume()) + ".")
				print("--The circumfrence is " + str(results.calc_cylinder_circ()) + ".\n")

			elif user_shape == "6":
				exit()

		else:
				# if user doesn't select a menu option:
		 		print("\nNo. \nType 1, 2, 3, 4, 5, or 6. \nLet's try again.\n")
		 		menu()

	except ValueError:
		# if user doesn't type a number:
		print("\nNo. \nType a number. \nLet's try again.\n")
		menu()

	menu()

if __name__ == '__main__':
    menu()
