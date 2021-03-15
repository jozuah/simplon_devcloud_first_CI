def reverse_digits(my_digits):
	reverse = 0
 	
	if my_digits > 0 : 
		while (my_digits > 0):
			remainder = my_digits % 10  
			reverse = (reverse * 10) + remainder  
			my_digits = my_digits // 10
	if my_digits < 0 :
		my_digits = my_digits * (-1)
		while (my_digits > 0):
			remainder = my_digits % 10
			reverse = (reverse * 10) + remainder
			my_digits = my_digits // 10
		reverse = reverse * (-1)

	return reverse  
