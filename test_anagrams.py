import unittest
from unittest import TestCase
from anagrams import find_anagrams, get_letter_counts


class TestAnagrams(TestCase):
	def test_get_letter_count(self):
		word = 'rose'
		#			a  b  c  d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
		expected = (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0)
		self.assertEqual(get_letter_counts(word), expected)
	
	def test_anagrams(self):
		words = ['rose', 'bike', 'sore', 'spaghetti', 'bad', 'dog', 'god']
		anagrams = find_anagrams(words)
		self.assertEqual(anagrams, [['rose', 'sore'], ['dog', 'god']])

	def test_anagrams_empty(self):
		words = ['rose', 'bike', 'spaghetti', 'bad', 'dog']
		anagrams = find_anagrams(words)
		self.assertEqual(anagrams, [])



if __name__ == '__main__':
	unittest.main()
