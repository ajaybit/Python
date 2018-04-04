def break_words (stuff):
	"""this function will break the full sentence in words"""
	words = stuff.split(' ')
	return words

def sort_words (words):
	"""Sort the words."""
	return sorted(words)
	
def print_first_word(words):
	"""Print the first word of the sentence"""
	word = word.pop(0)
	print word

def print_last_word(words):
	"""Print the last word of the sentence"""
	word = word.pop(-1)
	print word
	
def sort_sentence (sentence):
	"""Takes the full sentence and shor that"""
	words = break_words (sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted (sentence):
	words = sort_sentence (sentence)
	print_first_word(words)
	print_last_word(words)