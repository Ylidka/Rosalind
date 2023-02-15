# -*- coding: utf-8 -*-

from itertools import combinations

def MismatchList(kmer, d):
	    
	kmer_mismatches = [kmer]
	for i in range(1,d+1):
		        
		kmer_mismatches += CreateMismatches([[kmer, list(combo)] for combo in combinations(range(len(kmer)),i)])
	return kmer_mismatches

def CreateMismatches(swap_list):
	    
	nucleotides = 'ACGT'
	mismatch_list = []
	    
	swap = lambda string, ch, i: string[:index]+ch+string[index+1:]
	    
	if len(swap_list[0][1]) > 1:
		for kmer, indicies in swap_list:
			index = indicies[0]
			
			for nuc in filter(lambda n: n != kmer[index], nucleotides):
				mismatch_list.append([swap(kmer, nuc, index), indicies[1:]])

		return CreateMismatches(mismatch_list)
   
	else:
		for kmer, [index] in swap_list:
			#for nuc in [nuc for nuc in nucleotides if nuc != kmer[index]]:
			for nuc in filter(lambda n: n != kmer[index], nucleotides):
				mismatch_list.append(swap(kmer, nuc, index))

		return mismatch_list
    
if __name__ == '__main__':
	with open('rosalind_ba1i.txt') as input_data:
		dna, [k, d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]
	
    
	mismatch_dict = {}
	for i in range(len(dna)-k+1):
		for kmer in MismatchList(dna[i:i+k], d):
			if kmer in mismatch_dict:
				mismatch_dict[kmer] += 1
			else:
				mismatch_dict[kmer] = 1
	
    
	max_val = max(mismatch_dict.values())
	kmers = [item[0] for item in mismatch_dict.items() if item[1] == max_val]
	print (' '.join(kmers))
	with open('output_i.txt', 'w') as output_data:
		output_data.write(' '.join(kmers))