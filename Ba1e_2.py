# -*- coding: utf-8 -*-

f = open("rosalind_ba1e2.txt","r")

f1 = f.readline()
f2 = f.readline()

f1=f1.rstrip()
f2=f2.rstrip()

def kmercount(text,k,t):
    di,di_out ={},{};
    for i in range(len(text)-k+1):
        di[text[i:i+k]] = di.get(text[i:i+k],0)+1
    for i in di:
        if di[i] >= t: di_out[i]=di[i]
    return di_out
        
def Patterns_Forming_Clumps(genome, k, L, t):
    res=[]
    for i in range (len(genome)-L+1):
       res.extend(list(kmercount(genome[i:i+L],k,t).keys()))
    return set(res)


k,L,t = 10, 587, 19
genome= f1
#print(Patterns_Forming_Clumps(genome, k, L, t))
print(" ".join(Patterns_Forming_Clumps(genome,k,L,t)))
 