def generate_prime_num(n):
	if isinstance(n,int):
		if n>0:
			output=[]
			for num in range(1,n+1):
				count=0
				for i in range(1,num+1):
					d = num%i
					if d ==0:
						count +=1
				if count==2:
					output.append(num)
			return output
		else:
			raise ValueError("Only positive integers allowed")
			
	else:
		raise TypeError
