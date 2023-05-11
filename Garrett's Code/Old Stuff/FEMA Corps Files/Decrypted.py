# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:03:21 2021

@author: gellison
"""

lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alf = "abcdefghijklmnopqrstuvwxyz"
ALF = alf.capitalize()
bet = ""
yett = ""
count = 1
soup = {}
t = ""
w = ""
r= ""

def removeSpaces(bet):
    bet = bet.replace(' ','')
    return bet

def repalf():
    for a in alf:
        b = alf.find(a)
        lst[b] = inp[b]

def encrypt():
        for s in alf:
            z = bet.find(s)
            x = alf.find(s)
            soup[x + 97] = z + 97
                
        for s in alfA:
            z = betA.find(s)
            x = alfA.find(s)
            soup[x + 65] = z + 65
                        
def decrypt():
        for s in alf:
            z = bet.find(s)
            x = alf.find(s)
            soup[z + 97] = x + 97
    
        for s in alfA: 
            z = betA.find(s)
            x = alfA.find(s)
            soup[z + 65] = x + 65

def aff():
        inpa = input("Response >")
        if inpa == "yes" "no": 
            print("okay")

    
inp = input("Alphabet >  ")
inp1 = input("Phrase > ")
thorn = input("Thorn > ")

while thorn != "":
    if thorn == "y":
        thorn = True
        print("Understood. Perceptio est Omnia.")
        break
    else:
        thorn = False
        print("Understood. Creamus ergo Continuamus.")
        break
    
    
thet = inp1
repalf()

for x in lst:
    bet +=' '+x
bet = removeSpaces(bet)

alfA = alf.upper()
betA = bet.upper()

#decrypt()
encrypt()


phi = thet.translate(soup)

if thorn == True:
    phi = phi.replace("þ", "th")   
    phi = phi.replace("þ", "Th")

print(phi)

