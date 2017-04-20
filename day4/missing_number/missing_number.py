def find_missing(list1,list2):

	#check if both arguments are lists
	if isinstance(list1,list) and isinstance(list2,list):

		len_list1 = len(list1)
		len_list2 = len(list2)

		#if empty lists are passed as arguments return 0
		if len_list1==0 and len_list2==0:
			return 0

		#if list1 has more elements, then remove those of list2
		elif len_list1 >len_list2:
			for item in list2:
				if item in list1:
					list1.remove(item)
			if len(list1)==1:
				return list1[0]

		#if list2 has more elements inside then remove those of liost1
		elif len_list2 >len_list1:
			for item in list1:
				if item in list2:
					list2.remove(item)
			if len(list2)==1:
				return list2[0]

		# return 0 if list1==list2
		else:
			return 0
	else:
		raise TypeError("Only lists are allowed ")
def main():
	print find_missing([1, 2], [1, 2, 5])
if __name__ == '__main__':
	main()




