# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

y = ""
print('"%20" = space,\n"&body=" =body,\n"%0A%0A" = hard return,\n> Type "end" to finish')

x = input("Add Subject Here > ")
x = x.replace(" ", "%20")
x = x + '&body='

while y != "end":
    y = input("Add Body Line Here:")
    x = x + y
    x = x.replace(" ", "%20")  
    x = x + "%0A%0A"      


print(x)