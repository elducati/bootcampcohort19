import unittest 
from temp_convertor import convert_celcius_to_farenheit
class TempConvertortest(unittest.TestCase):
	#given in celcius = correct in F
	#data type for input
	#it it thorws an exception when data type is incorrect
	#check for null values -> throw an error

	def test_celcius_is_converted_to_farenheit(self):
		"""
			F =( celcius * 9/5) + 32 
		"""
		actual = convert_celcius_to_farenheit(10)
		expected = 50
		self.assertEqual(actual, expected,
						'celcius should convert to correc farenheit')
		self.assertEqual(convert_celcius_to_farenheit(20))
