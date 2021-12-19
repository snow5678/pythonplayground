def question1():
	number = float(input("Enter a number"))
	if number == 3:
		print ('third')
	elif number == 2:
		print ('second')
	elif number == 1:
		print ('first')
	elif number == 4 and number == 5:
		print ('top 5')		
	elif number >= 6 and number <= 10:
		print ('top 10')
	else 
		print ('Invalid Number')