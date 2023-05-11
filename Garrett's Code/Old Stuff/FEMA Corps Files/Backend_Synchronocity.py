Filepath = r"L:\IRC\NDRS 4611\605-Infrastructure Systems\Infrastructure Resources List"

#r"C:\Users\gellison\OneDrive - FEMA\Infrastructure RSF"
#r"C:\Users\gellison\OneDrive - FEMA\Desktop\LocalCopy\PersonalNotes\Python Resources\Programs\Root"
#r"C:\Users\gelliso1\OneDrive - FEMA\Desktop\FEMA Corps BACKUP\Ellison, Garrett (FEMA Corps)\Desktop\Synchronocity\Root.Test Folder"
#r"C:\Users\gelliso1\OneDrive - FEMA\Desktop\FEMA Corps BACKUP\Ellison, Garrett (FEMA Corps)\Desktop\Synchronocity\Root.Test Folder"
#r"L:\IRC\NDRS 4611\605-Infrastructure Systems\Infrastructure Resources List\General Resources"

import os
import glob
import re

fileinfo = ['filename','url']

def change(fileinfo, x, y):
    fileinfo[0] = x
    fileinfo[1] = y
    return fileinfo

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
#unused for the moment
def globber(fp):
    global dirname, dirpath, listname, listpath
    dirname = os.listdir(fp)
    dirpath = glob.glob(fp)
    listname = {fp : dirname}

#Verticle Counter
#Set a few variables:
#initdepth = Tallies the initial depth of the analyzed filepath
#findepth =  Calculates the Active depth as the program iterates through
initdepth = len(re.findall('/', fp))
print(initdepth)
startdepth = initdepth
findepth = 0
count = 0


#Boolean Flags
newtrunk = False
newlimb = False
newbough = False
newbranch = False

#Total Counter
cttrunk = 0
ctlimb = 0
ctbough = 0
ctbranch = 0
ctleaf = 0

#Horizontal Counter
deadend = False
cdtrunk=0
cdlimb=0
cdbough = 0
cdbranch = 0
cdleaf = 0

#Take Boolean Flags and output str of Flag if "True"
#Used to mark file appendage, and as a Boolean switch
def report(): 
    if newtrunk == True:
        return('Trunk')
    if newlimb == True:
        return('Limb')
    if newbough == True:
        return('Bough')
    if newbranch == True:
        return('Branch')

#Takes status of report() and acts as a switchboard to denote a DeadEnd (No further files to recurse through)
def reset(report):
    global cdbranch, cdbough, cdlimb, cdtrunk, deadend
    if report == "Trunk" and deadend == True:
        cdtrunk = 0
        deadend = False
        return('Reset')
    if report == "Limb" and deadend == True:
        cdlimb = 0
        deadend = False
        return('Reset')
    if report == "Bough" and deadend == True:
        cdbough = 0
        deadend = False
        return('Reset')
    if report == "Branch" and deadend == True:
        cdlimb = 0
        deadend= False
        return('Reset')
        
#Grab a clean filepath and append a child folder to the end
#Used to create a key for the next upcoming recurse, if not a DeadEnd
def stitch(x, y):
     y = str(y)
     y = wash(y)
     z = x + '/' + y
     z = wash(z)
     return z
    
#Aptly named because it runs a given os.walk tuple filepath (y) through a matrix
#There are 4 states of any given file: Yes/No Folders and Yes/No Files
#Inputs: Washed C://Filepath (os.walk[0]), or y in this case 
#        Subfolders (os.walk[1])
#        Subitems(os.walk[2])
#        Dictionary to overwrite
#Outputs: 
#        {y: ({Subfolder: ''}, Subitem)} 
     
def matrix(y, list1, list2, outputdict):
    global deadend
    templist = []
# Both lists are empty (filepath is a dead end)
    if not list1 and not list2:
        deadend = True
        print('Dead End')
        
        if type(outputdict) == list:
            outputdict.append('Dead End')
            return(outputdict)
            
        if type(y) == dict:
            y = str(y)
            outputdict[y] = 'Dead End'
            return(outputdict)
    
##Example of the use of Matrix   
#v = wash('C:/Users/gellison/OneDrive - FEMA/Desktop/LocalCopy/PersonalNotes/Python Resources/Programs/Root\\Trunk3\\Limb 31') 
#testlist1 = ['Bough  3 1 1']
#testlist2 = ['TestFile']
#tempdict= {}    
# 
#testlist3 = []
#testlist4 = []
#   
##print('\n', matrix(y0, testlist1, testlist2, tempdict))
#v0 = matrix(v, testlist1, testlist2, tempdict)   
#v1 = tempdict[v][0]
#print(v, v0, v1)
#
#v1 = matrix(v1, testlist3, testlist4, tempdict) 
#print('\n\n',tempdict)

    
# First list is empty  (no folders, yes files)
    elif not list1:
        deadend = True
        if type(outputdict) == list:
            outputdict.append([os.listdir(y),'url'])
            return(outputdict)
        
        outputdict[y] = list2
        return(outputdict)

# Second list is empty (yes folders, no files)
    elif not list2: 
        for z in list1:
            z = stitch(y, z)
            tempdict2 = {z : 'Empty'}
            templist.append(tempdict2)
            
        outputdict[y] = templist 
        return(outputdict)

# Neither list is empty (contains both folders and files)
    else: 
        for z in list1:
            x = stitch(y, z)
            tempdict2 = {x : ''}
            templist.append(tempdict2)
            
        for z in list2:
            x = stitch(y, z)
            templist.append([z, 'url'])
       
        if type(outputdict) == dict:
            outputdict[y] = templist   
            return(outputdict)
        
        if type(outputdict) == list:
            outputdict.append([os.listdir(y),'url'])
            return(outputdict)

templist = []

#Take updates to the lists, compile based on key given by os.walk[0] (y)
#def structure(y):     
#    boughpath[y] = branchlist
#    limbpath[y] = boughpath 
#    trunkpath[y] = limbpath
#    master[fp] = trunkpath

def depthcounter(fp):
    for x in os.walk(fp):
        initdepth = 0
        findepth = 0
        y = wash(x[0])
        depth = len(re.findall('/', y))
        print('\n',y)
        
    #Set final depth to measure level of recursion
        if depth - initdepth > findepth:        
            findepth = depth - initdepth
        else:
            pass
    #    print(y, depth)
        
#trunkpath = {}
#limbpath = {}
#boughpath = {}
#branchlist = []
    
def explanation():
    pass
"""
Okay, here we go. Below this is the main execution, it takes a filepath as input,
Recursively notes the filepaths and files of its children, then stitches them together
like russian nesting dolls to create a text string with the following format: 
    
{Rootfp: [{Trunk1fp: {[Limb1fp: {[Bough1fp: [[Branchdoc1, Branchurl1], [Branchdoc2, Branchurl2]]]]}}, Trunk2fp:{}, Trunk3doc}]}

cr.appendage = Filepath (dict key) of desired file/folder
cd.appendage = Index number of file/folder located inside of dictionary. Used to keep track of multiple items in a given folder.
ct.appendage = Total count of appendage type (i.e. total branches across all trunks)

To search for specific files/folders, use the following method:
    Start from the top, work your way down to the bottom. 
    If you're looking for a specific folder & given files, stop at cr.appendage
    If you're looking for a specific file within a given set of nested folders, stop at cd.appendage
  
Identify all items associated with a given trunk    
grove[cdtrunk]
Returns| {cdtrunk: [{limb: [{bough: [{branch: [[doc, docurl],[doc,docurl]]}}]}]

Identify all items inside of a given trunk (excluding the trunk)
grove[cdtrunk][crtrunk]
Returns| [{limb: [{bough: [{branch: [[doc, docurl],[doc,docurl]]}}]}

Identify all items associated with a given limb
grove[cdtrunk][crtrunk][cdlimb]
Returns| {limb: [{bough: [{branch: [[doc, docurl],[doc,docurl]]}}]}

Identify all items inside of a given limb (excluding the limb)
grove[cdtrunk][crtrunk][cdlimb][crlimb]
Returns| [{bough: [{branch: [[doc, docurl],[doc,docurl]]}]

Identify all items associated with a given bough
grove[cdtrunk][crtrunk][cdlimb][crlimb][cdbough]
Returns| {bough: [{branch: [[doc, docurl],[doc,docurl]]}}

Identify all items inside of a given bough (excluding the bough)
grove[cdtrunk][crtrunk][cdlimb][crlimb][cdbough][crbough]
Returns| [{branch: [[doc, docurl],[doc,docurl]]}]

Identify all items associated with a given branch
grove[cdtrunk][crtrunk][cdlimb][crlimb][cdbough][crbough][cdbranch]
Returns| {branch: [[doc, docurl]]}

Identify all items inside of a given branch (excluding the branch)
grove[cdtrunk][crtrunk][cdlimb][crlimb][cdbough][crbough][cdbranch][crbranch]   
Returns| [[doc, docurl],[doc,docurl]]

When a file has been found, extract the following information:
    Filename
        grove[cdtrunk]...[cd.appendage][0]
    URL of File
        grove[cdtrunk]...[cd.appendage][1]


I imagine it like creating a specific key to access a long hallway, you add a piece
for every door you encounter and use it to open all of the previous doors. 

"""   

#Contains the final output for the data 
grove=[]  

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#This is the beginning of the actual active part of the program
#Takes advantage of os.walk to recurse through all folders in a filepath
#uses two steps to get to the end: 
#First, tally and make note of active depth
#Second, rip apart the output tuple (x), wash it, and then determine where it is by:
#1. Setting the highest order limb to True (Trunk) to denote depth level
#2. Incrementing the Counter, begin Counting depth by incrementing the depth counter (cd.appendage)
#3. Checking to see if the output filepath is deeper than the one previous
#3a. If No, Increment the Horizontal Counter
#4. Store output according to schema by filtering y through the Matrix
#5. If current level is a DeadEnd, restart the Horizontal counter, then repeat above
#6. Set all higher order Boolean level flags to false, then recurse and repeat above

for x in os.walk(fp):
    trunkpath = {}
    print(x)
    y = wash(x[0])
    y0 = {}
    depth = len(re.findall('/', y))
    
#Set final depth to measure level of recursion
    if depth - initdepth > findepth:        
        findepth = depth - initdepth
    else:
        pass
#    print(y, depth)
        
#Check to see if os.walk is showing Trunk
    if depth - 1 == initdepth:
        global crtrunk
        limbpath = {}
        limbind = []
        newtrunk = True  
        crtrunk = y
        y0 = matrix(y, x[1], x[2], trunkpath)
        y1 = trunkpath[y]
        
#        print('\n',report(),'y=',y,'\n', 
#              'y0=',y0,'\n',
#              'y1=',y1,'\n\n')
#
#        print(trunkpath,'\n')
        grove.append(trunkpath)
        
        cttrunk += 1 
        cdtrunk += 1
        reset(report())

        
#Check to see if os.walk is showing Limb       
    elif depth - 2 == initdepth:
        global crlimb
        boughpath = {}
        newtrunk = False
        newlimb = True
        crlimb = y
        y0 = matrix(y, x[1], x[2], limbpath)
#        print(report(),'y=',y,'\n', 
#      'y0=',y0,'\n',
#      'y1=',y1,'\n\n')
        try:
            grove[cdtrunk - 1][crtrunk][cdlimb][crlimb] = limbpath[y]
        except:
            grove[cdtrunk - 1][crtrunk][cdlimb][crlimb] = 'Empty'   


        ctlimb += 1
        cdlimb += 1
        limbind.append(y)
        reset(report())
  
#Check to see if os.walk is showing Bough       
    elif depth - 3 == initdepth:
        global crbough
        newtrunk = False
        newlimb = False
        newbough = True
        crbough = y
        print(cdbough, crlimb) 
        y0 = matrix(y, x[1], x[2], boughpath)
#        print('\n',report(),'y=',y,'\n', 
#      'y0=',y0,'\n',
#      'y1=',y1,'\n\n')
#        print(grove[cdtrunk - 1][crtrunk][cdlimb - 1], cdtrunk, cdlimb, cdbough)
#        x = input('pause') 
        try:
            grove[cdtrunk - 1][crtrunk][cdlimb - 1][crlimb][cdbough][crbough] = boughpath[y]
        except:
            try:
                grove[cdtrunk - 1][crtrunk][cdlimb - 1][crlimb][cdbough][crbough] = 'Empty'
            except: 
                grove[cdtrunk][crtrunk][cdlimb - 1][crlimb][cdbough][crbough] = 'Empty'
              
        ctbough += 1
        cdbough += 1
        reset(report())

        
#Check to see if os.walk is showing Branch        
    elif depth - 4 == initdepth:
        global crbranch
        branchlist = []
        newtrunk = False
        newlimb = False
        newbough = False
        if newbranch == True:
            branchlist = []
        newbranch = True
        y0 = matrix(y, x[1], x[2], branchlist)
#        y1 = branchlist[y]

        print(report(),'y=',y,'\n', 
      'y0=',y0,'\n',
      'y1=',y1,'\n\n')
        
        try:
            grove[cdtrunk - 1][crtrunk][cdlimb - 1][crlimb][cdbough - 1][crbough][cdbranch][y] = boughpath[y]
        except:
            grove[cdtrunk - 1][crtrunk][cdlimb - 1][crlimb][cdbough - 1][crbough][cdbranch][y] = y
        
        ctbranch += 1
        cdbranch += 1
        reset(report())



# {Rootfp: {Trunk1fp: {Limb1fp: {Bough1fp: [[Branchdoc1, Branchurl1], [Branchdoc2, Branchurl2]}}, Trunk2fp:{}, Trunk3doc}}
# Then....
#    For Rootfp:
#       For Trunkfp:
#           TrunkDict: {LimbDict}
#            For Limbfp:
#               LimbDict: ({Branchlist}, x[2])
#               For Boughfp:   
#                   Boughfp: {Branchlist} 
#                   Branchlist.append([Branchdoc1, Branchurl1])
#    
   
#print('\n',findepth,master)
        
#For debugging: Print keys of trunkpath
#for key,value in trunkpath.items():
#	print('\n',key, ':', value)
 
#Construct Metadata for Grove, including Max Depth, and Total Appendages

#Boolean Flags
#newtrunk = False
#newlimb = False
#newbough = False
#newbranch = False

#Append a Metadata trunk to analyze compiled output data
metadata = {
'Initial Depth': startdepth,
'Final Depth' : findepth,
'Total Trunks': cttrunk,
'Total Limbs': ctlimb,
'Total Boughs': ctbough,
'Total Branches': ctbranch,
'Total Leaves': ctleaf
    }

grove.append(metadata)
       
#Write grove data directly to .txt     
output = open("output.txt", "w")
n = output.write(str(grove))
output.close()

##write a Human Readable Output String Version
#DebugOutput = open("DebugOutput.txt","w")
#format = grove.format
#n = DebugOutput.write(str(grove))
#output.close()

print(grove)
#grove[cdtrunk][crtrunk][cdlimb][crlimb][cdbough][crbough][cdbranch][crbranch]


    
    
    
    
    
    
    
    
    
    
    
    