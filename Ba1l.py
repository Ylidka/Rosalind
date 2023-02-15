# -*- coding: utf-8 -*-

def symtonum(s):
    sh='ACGT'
    return sh.index(s)

def ptntonum(pat):
    if len(pat)==0:
        return 0
    symbol = pat[-1]
    prefix = pat[:-1]
    return (4*ptntonum(prefix)+symtonum(symbol))

if __name__=='__main__':
    pattern = 'GTCATGCCTAGCTTGGGCTCTAAGCGCC'
    print(ptntonum(pattern))
    