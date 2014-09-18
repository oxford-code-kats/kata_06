def get_letter_counts(word):
	pass
def find_anagrams(w_list):
	count_dict = {}
	for word in w_list:
		counts = get_letter_counts(word)
		try:
			count_dict[counts].append(word)
		except KeyError:
			count_dict[counts] = [word]

	output = []
	for words in count_dict.values():
		if len(words) >= 2:
			output.append(words)
	return output