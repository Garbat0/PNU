Filepath = r"C:\Users\gellison\OneDrive - FEMA\Desktop\LocalCopy\PersonalNotes\Python Resources\Programs\Root"

import os
import glob
import re

#wash filepaths for use in various functions
def wash(q):
    q = q.replace("[","")
    q = q.replace("]","")
    q = q.replace(os.sep, '/')
    q = q.replace('//','/')
    q = q.replace("'","")
    return q 

fp = wash(Filepath)
#glob names of files in directory
def globber(fp):
    global dirname, dirpath, listname, listpath
    dirname = os.listdir(fp)
    dirpath = glob.glob(fp)
    listname = {fp : dirname}


master: {fp: ''}
trunkpath = {}
count = 0
Trunk = True

globber(fp)

def stitch(x, y):
     y = str(y)
     y = wash(y)
     z = x + '/' + y
     z = wash(z)
     return z
 
def recurser(filepath):
    for x in filepath:
        
        pass


#stitch filenames into directory, begin creation of Trunk list
for x in dirname:
    ind = dirname.index(x)
    x = wash(x)
    z = fp + '/' + x
    trunkpath[z] = ''
    limbpath = {}
    limbname = []
    count = 0
    depth = 1
#   walk through each Trunk, count depth, assemble files 
    for limb in os.walk(z):
        templist = []
        a = limb[0]
        astr = str(a)
        
#       a = filepath
        b = limb[1]
#       b = Sub-Folders inside of folder
        c = limb[2]
#       c = Files inside of folder       
#        print(b, c,'\n')
        if not b:
            print("No Subfolders",'\n')
            limbname.append(templist)
            break
            
        else:
            for x in b:
                z = stitch(a,x)
                print(count,depth, z)
                recurser(z)                    
                depth += 1
            
            
            
            count += 1
    trunkpath[z] = limbpath
#        if not b:
##       Checks to see if this folder is a dead end            
#            limbname.append(c)
#            if not c:
#                continue
#            print('file',c)
#            

        
#print(trunkpath)       
for x in os.walk(fp):
    print(x)

#class recurser(self, filepath):
#    __init__(self):
#        
#        
#        
#        def _simple(self, _complex, _simple):
#            for x in filepath: 
#                templist = []
#                templist.append[x]
#            return(templist)
#        
#        
#        
#        def _complex():
#            pass
##            return(x)
        
            
    
#    print(limbname)
#        limbpath = {x: ""}
        
    #recompile lists/dictionaries
#    trunkpath[z] = limbpath
    
    
#print(trunkpath)
#
            
#dicst = {1 : 0,
#         5 : 0,
#         8 : 0}
#print(dicst.keys())


#print(listname, '\n', listpath)

#for x in rootglob:
#    pass
#class A:
#    def whoami(self):
#        print(type(self).__name__)
#
#class B(A):
#    pass
#
#o = B()
#o.whoami()

#
#class Vehicle:
#    def __init__(self, brand, model, type):
#        self.brand = brand
#        self.model = model
#        self.type = type
#        self.fuel_size = 14
#        self.fuel_level = 0
#        
#    def fuel_up(self):
#        self.fuel_level = self.fuel_size
#        print('All Full!')
#        
#    def drive(self, x):
#        if x > self.fuel_level: 
#        self.fuel_level = self.fuel_level - x             
#        print(f'The {self.model} is now driving', f'{x} units.')
##        
#Honda = Vehicle('Honda', 'Ridgeline', 'Truck')
#print(Honda.brand, Honda.model, Honda.type, Honda.fuel_size, Honda.fuel_level)
#print('\n', Honda.fuel_level,'\n')
#Honda.fuel_up()
#print('\n', Honda.fuel_level)
#Honda.drive(15)
#print('\n', Honda.fuel_level)