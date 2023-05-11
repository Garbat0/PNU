# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:27:20 2023

@author: gelliso1
"""
import re
firstnames = []
lastnames = []


names = input("Input Names Here> ")
words = names.replace("•\t","^")
words = words.replace("\n"," ")
words = words.split(" ")
count = 0
print(words)

for name in words:
    print(name)
    pattern = "^"
    match = re.match(pattern, r"name")
    if count == 1:
        count = 0
        lastnames.append(name)
        continue
    
    if match:
        count = 1
        name = name.replace("^","")
        templist = list(name)
        print('temp',templist,'last',lastnames,'first',firstnames)
#        templist[1] = "."; 
#        templist[2] = " "; 
#        del templist[3:]
#        name = str(templist)
#        firstnames.append(name)
        
    else: 
        continue
    

    

        
        
    
    
