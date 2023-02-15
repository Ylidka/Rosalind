# -*- coding: utf-8 -*-

def numtosym(i):
    sh='ACGT'
    return sh[i]

def numtopat(num,k):
    if k == 1:
        return numtosym(num)
    prefind = num//4
    r = num%4
    sym = numtosym(r)
    prefptn = numtopat(prefind, k-1)+sym
    return prefptn

if __name__=='__main__':
    num = 5998
    k = 10
    print(numtopat(num,k))
    
   