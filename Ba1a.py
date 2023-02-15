# -*- coding: utf-8 -*-

f = open("dataset_2_7.txt","r")

f1 = f.readline()

f2 = f.readline()

f1=f1.rstrip()
f2=f2.rstrip()

def PatternCount(text, pattern):  
    count = 0  
    for i in range(len(text)-len(pattern)+1):  
        if text[i:i+len(pattern)] == pattern:  
            count=count+1  
    return count  

if __name__=='__main__':
    f1 ='GCGCG'
    f2 = 'GCG'
    print(PatternCount(f1, f2)) 