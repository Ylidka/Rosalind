# -*- coding: utf-8 -*-

f = open("rosalind_ba1g.txt","r")

f1 = f.readline()
f2 = f.readline()

f1=f1.rstrip()
f2=f2.rstrip()

def Hamming_Distance(p,q):
    count = 0
    i=0
    while(i < len(p)):
        if(p[i] != q[i]):
            count +=1
        i += 1
    return count

#p="GGGCCGTTGGT"
#f="GGACCGTTGAC"
print(Hamming_Distance(f1,f2))
        