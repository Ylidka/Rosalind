# -*- coding: utf-8 -*-

f = open("rosalind_ba1d.txt","r")

f1 = f.readline()
f2 = f.readline()

f1=f1.rstrip()
f2=f2.rstrip()

def Occurrences(genome, pattern):
    
    start = 0
    indexes = []
    while True:
        start = genome.find(pattern, start)
        if start > 0:
            indexes.append(start)
        else:
            break

        start += 1

    return indexes
        

output= Occurrences(f2, f1)
#print (output)

outputString =' '.join(str(e) for e in output)

with open("output_d.txt", "a") as file:
    file.write(outputString)
