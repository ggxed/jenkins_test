import unittest
from Main import rgb_to_y


class Test_rgb_to_y(unittest.TestCase):

	def test_values(self):
		self.assertRaises(ValueError, rgb_to_y, -2, -3, -2)
		self.assertRaises(ValueError, rgb_to_y, -2, 3, 2)
		self.assertRaises(ValueError, rgb_to_y, 2, -3, 2)
		self.assertRaises(ValueError, rgb_to_y, 2, 3, -2)