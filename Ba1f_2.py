# -*- coding: utf-8 -*-

f = open("rosalind_ba1f.txt","r")

f1 = f.readline()

f1=f1.rstrip()

sequence = f1

def Find_Skew(sequence):
	c = 0
	min_skew = 0
	skew_list = []
	index = 0
	for i in sequence:
		index += 1
		if i == 'C':
			c -= 1
		if i == 'G':
			c += 1
		
		if c < min_skew:
			skew_list = [index]
			min_skew = c
		if c == min_skew and index not in skew_list:
			skew_list.append(index)	
	return skew_list	

FS = Find_Skew(sequence)
FS_String =' '.join(str(e) for e in FS)

print(FS_String)