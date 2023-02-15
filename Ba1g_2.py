# -*- coding: utf-8 -*-

f = open("rosalind_ba1g.txt","r")

f1 = f.readline()
f2 = f.readline()

f1=f1.rstrip()
f2=f2.rstrip()

def Hamming_Distance(string1, string2): 
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance
#p="GGGCCGTTGGT"
#f="GGACCGTTGAC"
if __name__ == "__main__":
    string1 = f1
    string2 = f2
    print(Hamming_Distance(f1,f2))