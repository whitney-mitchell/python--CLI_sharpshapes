import math

class Shape:
	pass

class Circle(Shape):
# init and do math for circle

	def __init__(self, radius):
		self.radius = radius

	def calc_circle_area(self):
		self.area = round(math.pi * (self.radius**2), 2)
		return self.area

	def calc_circle_circ(self):
		self.circ = round((2 * math.pi * self.radius), 2)
		return self.circ

class Cylinder(Circle):
# init and do math for cylinder
	pass

	# def __init__(self, radius, height):
		# self.radius = radius
		# self.height = height
	# def calc_cylinder_output(self):
		# math
class Square(Shape):
# init and do math for square

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
		self.area = round(self.base * self.height)
		return self.area

class Cube(Square):
# init and do math for cube
	pass
	# def __init__(self, height):
		# self.height = height

	# def calc_cube_output(self):
		# math

def menu():

	print("Select a shape by its number:")
	print("1. Circle \n2. Square \n3. Rhombus \n4. Cube \n5. Cylinder \n6. Quit")

	user_shape = input("> ")

	try:
		if int(user_shape) > 0 and int(user_shape) < 7 :
			# if else statements ---
			if user_shape == "1":
				print("What would you like the radius of your circle to be?")
				radius = int(input("> "))

				results = Circle(radius)
				print("The area of your circle is " + str(results.calc_circle_circ()) + ". \nThe circumference is " + str(results.calc_circle_area()) + ".\n")

			elif user_shape == "2":
				print("What would you like the length of your square to be?")
				length = int(input("> "))

				results = Square(length)
				print("The area of your square is " + str(results.calc_square_area()) + ". \nIt has 4 sides.\n")

			elif user_shape == "3":
				print("What would you like the height of your rhombus to be?")
				height = int(input("> "))

				print("What about the length of the base?")
				base = int(input("> "))

				results = Rhombus(base, height)
				print("The area of your rhombus is " + str(results.calc_rhombus_area()) + ". \nIt has 4 sides.\n")

			# elif user_shape =="4":

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
	# if choice != "6":
					# self.show_menu()
	 	# error handling inside the loop (for numbers)
	# error handling outside (for numbers, but of the selections)

if __name__ == '__main__':
    menu()
