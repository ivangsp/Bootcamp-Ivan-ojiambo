def fizz_buzz(num):
	if isinstance(num, int):
		if num <=0:
			return('Invalid Argument')
		else:
			if num%5==0 and num%3==0:
				return 'fizzBuzz'
				
			elif num%3==0:
				return 'fizz'
				
			elif num %5==0:
				return 'buzz'
			else:
				return num
	else:
		return('Invalid Argument')
