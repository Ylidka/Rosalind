# -*- coding: utf-8 -*-

with open("rosalind_ba1c.txt", "r") as file:
    seq=file.read()

seq=seq.rstrip()

input=seq
def inversComplement(input):
    output = ''
    for letter in input:
        letter = letter.upper()

        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

    return(output[::-1])

seq2=inversComplement(input)

with open("output_с2.txt", "a") as file:
    file.write(seq2)
