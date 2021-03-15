from reverse_string import reverse_string
from reverse_number import reverse_number
from reverse_digits import reverse_digits

def main ():
	my_string = "Hello world"
	print("Ma string:", my_string)
	my_reverse_string = reverse_string(my_string)
	print("Ma string inversée:", my_reverse_string)

	my_number = -1234
	print("Mon nombre :", my_number)
	my_reverse_number = reverse_number(my_number)
	print("Mon nombre opposé:", my_reverse_number)

	my_reverse_digits = reverse_digits(my_number)
	print("Mon nombre inversé:", my_reverse_digits)	


main()
