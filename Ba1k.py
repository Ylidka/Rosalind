# -*- coding: utf-8 -*-

from collections import Counter


filename = 'rosalind_ba1k.txt'

def lex_kmers(alphabet, n):
	strings = []

	def helper(curr):
		if len(curr) == n:
			strings.append(curr)
		else:
			for char in alphabet:
				helper(curr + char)

	helper('')		
	return strings

def freq_array(text, k):
	c = Counter([text[i : i + k] for i in range(len(text) - k + 1)])
	kmers = lex_kmers(['A', 'C', 'G', 'T'], k)
	return [c.get(kmer, 0) for kmer in kmers]

def main():
	with open(filename) as f:
		text = f.readline().strip()
		k = int(f.readline().strip())
	print(*freq_array(text, k))
        

if __name__ == '__main__':
	main()