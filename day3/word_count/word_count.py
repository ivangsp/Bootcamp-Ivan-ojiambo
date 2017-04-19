# -*- coding: utf-8 -*-
def words(words):
	if words!=" ":
		output={}
		splited_words=words.split()
		for word in splited_words:
			if '\n' in word:
				splited_words.remove(word)
				splited_words+= word.split('\n')

			if '\t' in word:
				splited_words.remove(word)
				splited_words+= word.split('\t')

		for each_word in  splited_words:
			try:
				output[int(each_word)] = splited_words.count(each_word)
			except ValueError:
				output[each_word] = splited_words.count(each_word)


		return output

	else:
		raise ValueError("Enter argument in the function")
def main():
	print words('Hello Andela  ivan'),
if __name__=='__main__':
	main()