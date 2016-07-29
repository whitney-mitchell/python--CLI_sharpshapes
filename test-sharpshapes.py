import unittest
from sharpshapes import *

class TestSharpShapes(unittest.TestCase):

	# @classmethod
	# def setUpClass(self):
	# 	self.shape = Shape()

	def test_circle_results_area(self):
		shape = Circle(4)
		self.assertEqual(25.13, shape.calc_circle_circ())

	def test_circle_results_circ(self):
		shape = Circle(3)
		self.assertEqual(28.27, shape.calc_circle_area())

	def test_cylinder_results(self):
	# should return circ, area, vol, sides
		pass

	def test_square_area(self):
		shape = Square(4)
		self.assertEqual(16, shape.calc_square_area())

	def test_rhombus_results(self):
	# should return area, sides
		shape = Rhombus(6, 4)
		self.assertEqual(24, shape.calc_rhombus_area())

	def test_cube_results(self):
	# should return area, vol, sides
		pass

if __name__ == '__main__':
		unittest.main()
# This exercise involves creating a system that generates myriad shapes.
# Build a command line tool that does the following:

# Outputs a numbered list of possible shapes to be built.
# Allows user to select one of the choices.
# After shape type is chosen, ask for size information.
# Radius for circles.
# Width/height for squares and rectangles.
# Radius/height for cylinders.
# etc..
# After basic size information is entered, the program will output circumference/area/volume
# of the shape, and the number of sides for the shape.
# Note: Keep your code DRY.
# Class inheritance can definitely be used to your advantage in this exercise.

# Step 1 Example

# Select a shape:
# 1. Circle
# 2. Square
# 3. Rhombus
# 4. Cube
# 5. Cylinder
# >

# Step 2 Example

# You chose Cube.

# Enter the height, width, and depth separated by commas
# > 5,4,8

# Step 3 Example

# The total volume of the cube is 160.


# Requirements

# Write your unit test suite first.

# Start with a basic Shape class. Then plan out every specific
# shape that you want to derive from it, write tests verifying type checking,
# and the expected output of every method on your shapes.
