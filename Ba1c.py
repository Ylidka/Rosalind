# -*- coding: utf-8 -*-

with open("rosalind_ba1c.txt", "r") as file:
    seq=file.read()

seq=seq.rstrip()

def ComplimentSeq(t):
    r=""
    for i in range(len(t)):
        if t[i]=='A': r=r+'T'
        if t[i]=='T': r=r+'A'
        if t[i]=='G': r=r+'C'
        if t[i]=='C': r=r+'G'
    return(r)

seq2=ComplimentSeq(seq)

with open("output_с.txt", "a") as file:
    file.write(seq2)