import unittest
from function_prime_number import prime_number

class Prime_numberTest(unittest.TestCase):
	#check for number below 2 and return false
	#if number in range is divisible by two break
	#if number is prime append to empty list
	def test_prime_number(self):
		expected = [2, 3, 5]
		self.assertEqual( prime_number(7),expected)
	def test_type(self):
		expected = [2, 3, 5]
		self.assertIsInstance(expected, list)
	def test_n_as_int(self):
		expected = [2, 3, 5]
		for i in expected:
			self.assertIsInstance(i, int )
	def test_prime_number_for_less_than_two(self):
		result = prime_number(1)
		self.assertFalse(result)
	def test_for_negative_numbers(self):
		result = prime_number(-5)
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()