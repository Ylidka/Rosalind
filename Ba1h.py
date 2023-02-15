# -*- coding: utf-8 -*-

f = open("rosalind_ba1h2.txt","r")

f1 = f.readline()
f2 = f.readline()
f3 = f.readline()

f1=f1.rstrip()
f2=f2.rstrip()
f3=f3.rstrip()

d = int(f3)

from hamming_distance import Hamming_Distance

def Approximate_pattern(pattern, seq, d):
    res = ''
    l = len(pattern)
    for i in range(len(seq)-l):
        if Hamming_Distance(pattern, seq[i:i+l]) <= d:
            res += str(i) + ' '
    return res

#print(Approximate_pattern(a,b,d2))

with open("output_h.txt", "a") as file:
    file.write(Approximate_pattern(f1,f2,d))