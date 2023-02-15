# -*- coding: utf-8 -*-

from itertools import combinations
from collections import defaultdict
from Ba1c_2 import inversComplement as rev_comp
from Ba1i_2 import MismatchList as kmer_mismatches


def freq_words_with_mm_and_rev_comp(seq, k, d):
    
    kmer_freq = defaultdict(int)
    for i in range(len(seq)-k+1):
        kmer_freq[seq[i:i+k]] += 1
        kmer_freq[rev_comp(seq[i:i+k])] += 1

        mismatch_count = defaultdict(int)
    for kmer, freq in kmer_freq.items():
        for mismatch in kmer_mismatches(kmer, d):
            mismatch_count[mismatch] += freq

    
    max_count = max(mismatch_count.values())
    return sorted([kmer for kmer, count in mismatch_count.items() if count == max_count])


def main():
    
    with open('rosalind_ba1j.txt') as input_data:
        seq = input_data.readline().strip()
        k, d = map(int, input_data.read().strip().split())

    
    most_freq_kmers = freq_words_with_mm_and_rev_comp(seq, k, d)
    
    print (' '.join(most_freq_kmers))
    with open('output_j.txt', 'w') as output_data:
        output_data.write(' '.join(most_freq_kmers))

if __name__ == '__main__':
    main()