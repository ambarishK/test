# import modules


import re
import sys
import regex
from collections import defaultdict


#read file and get fasta lines



File=open(sys.argv[1], 'r').read().splitlines()


#### Get All motifs with exact match

print("-------------------------All motifs with exact match :--------------------")

def motifWithExactMatch():

### List of regular expressions. 

 L=['W[KRH]..[ALYFIMVW][DE]']

 for line in File:
  dic = defaultdict(list)
  if line[0]=='>':
   print (line)
  if line[0]!='>':
   count = 0
   indexPositions = []
   listOfMatchObs = []
   
### Get motifs on line for each regular expression into the list. 
 
   for l in L:                        
     regexPattern = re.compile(l)
     mainStr=line
     iteratorOfMatchObs = regexPattern.finditer(mainStr)
     
### Get list of motifs and their count on line.    
    
     for matchObj in iteratorOfMatchObs:
       indexPositions.append(matchObj.start())
       listOfMatchObs.append(matchObj.group())
       count = count + 1
       
### Print outputs.

   for i in range(len(listOfMatchObs)):
       dic[listOfMatchObs[i]].append(str(indexPositions[i]))
   for i in dic:
       print(i," ".join(dic[i]))

   print("Count of found motifs on line:", count)
     
#### Function call.
motifWithExactMatch()





#### Get All motifs with five residues match

print("-------------------------All motifs with five residues match :--------------------")

def motifWithFiveResiduesMatch():

### List of regular expressions. 

 L=['W[KRH]..[ALYFIMVW]','[KRH]..[ALYFIMVW][DE]']

 for line in File:
  dic = defaultdict(list)
  if line[0]=='>':
   print (line)
  if line[0]!='>':
   count = 0
   indexPositions = []
   listOfMatchObs = []
   
### Get motifs on line for each regular expression into the list. 
 
   for l in L:                        
     regexPattern = re.compile(l)
     mainStr=line
     iteratorOfMatchObs = regexPattern.finditer(mainStr)
     
### Get list of motifs and their count on line.    
    
     for matchObj in iteratorOfMatchObs:
       indexPositions.append(matchObj.start())
       listOfMatchObs.append(matchObj.group())
       count = count + 1
       
### Print outputs.

   for i in range(len(listOfMatchObs)):
       dic[listOfMatchObs[i]].append(str(indexPositions[i]))
   for i in dic:
       print(i," ".join(dic[i]))

   print("Count of found motifs on line:", count)
     
#### Function call.
motifWithFiveResiduesMatch()




#### Get All motifs with four residues match

print("-------------------------All motifs with four residues match :--------------------")

def motifWithFourResiduesMatch():

### List of regular expressions. 

 L=['W[KRH]..','..[ALYFIMVW][DE]','[KRH]..[ALYFIMVW]']

 for line in File:
  dic = defaultdict(list)
  if line[0]=='>':
   print (line)
  if line[0]!='>':
   count = 0
   indexPositions = []
   listOfMatchObs = []
   
### Get motifs on line for each regular expression into the list. 
 

   for l in L:                        

     regexPattern = re.compile(l)
     mainStr=line
     iteratorOfMatchObs = regexPattern.finditer(mainStr)
     
### Get list of motifs and their count on line.    
    
     for matchObj in iteratorOfMatchObs:
       indexPositions.append(matchObj.start())
       listOfMatchObs.append(matchObj.group())
       count = count + 1
       
### Print outputs.

   for i in range(len(listOfMatchObs)):
       dic[listOfMatchObs[i]].append(str(indexPositions[i]))
   for i in dic:
       print(i," ".join(dic[i]))

   print("Count of found motifs on line:", count)
     
#### Function call.
motifWithFourResiduesMatch()











