# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:02:16 2022

@author: gellison
"""
import re

notter = input("input JQL text to NOT >>>  ")
notter = notter.replace('text ~ "', 'text !~ "')
notter = notter.replace('OR', 'AND')
print('\n',notter)
