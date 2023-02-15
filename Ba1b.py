# -*- coding: utf-8 -*-

f = open("dataset_2_10.txt","r")

f1 = f.readline() #строка
f2 = f.readline() #длина патерна

f1=f1.rstrip()
f2=f2.rstrip()


#print(f1,f2)

def PatternCount(text, pattern):  
     count = 0  
     for i in range(len(text)-len(pattern)+1):  
         if text[i:i+len(pattern)] == pattern:  
             count=count+1  
     return count  
PatternCount(f1, f2)

f2=int(f2)

def FrequentPattern(text, k):
    dic={}
    count=0
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        if pattern not in dic:
            countpattern=PatternCount(text, pattern)
            
            dic.update({pattern:countpattern})
            if(count<countpattern): count=countpattern
    for key,value in dic.items():
        if value==count: 
            print(key)

FrequentPattern(f1,f2)


        